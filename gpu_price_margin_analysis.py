import csv
import re

def normalize_model_name(name):
    name = name.lower()
    brands = ["asus", "msi", "gigabyte", "zotac", "colorful", "evga", "pny", "inno3d", "leadtek", "manli", "sapphire", "powercolor", "xfx", "nvidia", "amd"]
    for brand in brands:
        name = name.replace(brand, "")
    name = re.sub(r"\b\d{1,3} ?gb\b", "", name)
    descriptors = ["gaming", "dual", "ventus", "trio", "tuf", "rog", "strix", "oc", "winforce", "eagle", "prime", "shadow", "amp", "ultra", "twin", "edition", "promo", "white", "black", "advanced", "super", "nb", "duo", "sff", "ice", "vanguard", "suprim", "astral", "inspire", "battle ax", "polax fox", "plus", "trinity"]
    for desc in descriptors:
        name = name.replace(desc, "")
    name = re.sub(r"[^a-z0-9 ]", "", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name

# --- Parse current price files ---
def parse_current_prices(file_path):
    prices = {}
    try:
        f = open(file_path, encoding='utf-8-sig')
        reader = csv.DictReader(f)
        for row in reader:
            model = normalize_model_name(row.get('Nama', row.get('Nama', '')))
            price_str = row.get('Harga', '').replace('Rp', '').replace('.', '').replace(',', '').strip()
            try:
                price = int(price_str)
            except:
                continue
            prices[model] = price
        f.close()
    except UnicodeDecodeError:
        f = open(file_path, encoding='latin1')
        reader = csv.DictReader(f)
        for row in reader:
            model = normalize_model_name(row.get('Nama', row.get('Nama', '')))
            price_str = row.get('Harga', '').replace('Rp', '').replace('.', '').replace(',', '').strip()
            try:
                price = int(price_str)
            except:
                continue
            prices[model] = price
        f.close()
    return prices

# --- Parse 2022 price file ---
def parse_2022_prices(file_path):
    prices = {}
    try:
        f = open(file_path, encoding='utf-8-sig')
        reader = csv.DictReader(f)
        for row in reader:
            model = normalize_model_name(row.get('name', row.get('model', '')))
            price_str = row.get('price', '').replace('$', '').replace(',', '').strip()
            try:
                price = float(price_str)
            except:
                continue
            prices[model] = price
        f.close()
    except UnicodeDecodeError:
        f = open(file_path, encoding='latin1')
        reader = csv.DictReader(f)
        for row in reader:
            model = normalize_model_name(row.get('name', row.get('model', '')))
            price_str = row.get('price', '').replace('$', '').replace(',', '').strip()
            try:
                price = float(price_str)
            except:
                continue
            prices[model] = price
        f.close()
    return prices

# --- Parse 2024 price file ---
def parse_2024_prices(file_path):
    prices = {}
    try:
        f = open(file_path, encoding='utf-8-sig')
        reader = csv.DictReader(f)
        for row in reader:
            model = normalize_model_name(row.get('GPU Model', ''))
            price_str = row.get('Best US Price', '').replace('$', '').replace(',', '').strip()
            try:
                price = float(price_str)
            except:
                continue
            prices[model] = price
        f.close()
    except UnicodeDecodeError:
        f = open(file_path, encoding='latin1')
        reader = csv.DictReader(f)
        for row in reader:
            model = normalize_model_name(row.get('GPU Model', ''))
            price_str = row.get('Best US Price', '').replace('$', '').replace(',', '').strip()
            try:
                price = float(price_str)
            except:
                continue
            prices[model] = price
        f.close()
    return prices

# --- Main Analysis ---
def main():

    USD_TO_IDR = 16000  # Fixed rate
    # Read combined average prices as current prices
    current_prices = {}
    with open('gpu_data_combined_avg_by_query.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            model = row.get('Model (Query)', '').strip()
            price_str = row.get('Average Price (IDR)', '').replace(',', '').strip()
            try:
                price = int(price_str)
            except:
                price = None
            if model and price:
                current_prices[model] = price

    prices_2022 = parse_2022_prices("./gpu_specs_prices.csv")
    prices_2024 = parse_2024_prices("./GPU_Price_Index.csv")

    def fuzzy_lookup(model, price_dict):
        # Try exact match first
        if model in price_dict:
            return price_dict[model]
        # Try partial match
        for k in price_dict:
            if model in k or k in model:
                return price_dict[k]
        return ''

    with open('gpu_price_margin_analysis.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Model', 'Current Price (IDR)', '2022 Price (IDR)', '2024 Price (IDR)', 'Margin vs 2022 (%)', 'Margin vs 2024 (%)'])
        for model, cur_price in current_prices.items():
            norm_model = normalize_model_name(model)
            price_2022 = fuzzy_lookup(norm_model, prices_2022)
            price_2024 = fuzzy_lookup(norm_model, prices_2024)
            price_2022_idr = price_2022 * USD_TO_IDR if price_2022 else ''
            price_2024_idr = price_2024 * USD_TO_IDR if price_2024 else ''
            margin_2022 = ''
            margin_2024 = ''
            if price_2022:
                margin_2022 = round((cur_price - price_2022_idr) / price_2022_idr * 100, 2)
            if price_2024:
                margin_2024 = round((cur_price - price_2024_idr) / price_2024_idr * 100, 2)
            writer.writerow([model, cur_price, price_2022_idr, price_2024_idr, margin_2022, margin_2024])
    print('Analysis complete. Results saved to gpu_price_margin_analysis.csv.')

if __name__ == '__main__':
    main()
