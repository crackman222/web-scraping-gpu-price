import csv

# List of queries/models
queries = [
    "rtx 2060","rtx 2060 super", "rtx 2070","rtx 2070 super", "rtx 2080", "rtx 2080 super", "rtx 2080 ti",
    "rtx 3050 6g", "rtx 3050 8g", "rtx 3060", "rtx 3060 ti", "rtx 3070", "rtx 3070 ti", "rtx 3080", "rtx 3080 ti", "rtx 3090", "rtx 3090 ti",
    "rtx 4060", "rtx 4060 ti", "rtx 4070", "rtx 4070 super", "rtx 4070 ti", "rtx 4070 ti super", "rtx 4080", "rtx 4080 super", "rtx 4090",
    "rtx 5050", "rtx 5060", "rtx 5060 ti", "rtx 5070", "rtx 5070 ti", "rtx 5080", "rtx 5090"
]

model_prices = {q: [] for q in queries}

# Process gpu_data_toped.csv
with open('gpu_data_toped.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        query = row.get('Query', '').strip()
        price_str = row.get('Harga', '').replace('Rp', '').replace('.', '').replace(',', '').strip()
        try:
            price = int(price_str)
        except:
            continue
        if query in model_prices:
            model_prices[query].append(price)

# Process gpu_data_kgal.csv
with open('gpu_data_kgal.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row.get('Nama', '').lower()
        price_str = row.get('Harga', '').replace('Rp', '').replace('.', '').replace(',', '').strip()
        try:
            price = int(price_str)
        except:
            continue
        # Match query by checking if query string is in name
        for q in queries:
            if q in name:
                model_prices[q].append(price)
                break

# Output average prices
with open('gpu_data_combined_avg_by_query.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Model (Query)', 'Average Price (IDR)', 'Sample Size'])
    for model, prices in model_prices.items():
        if prices:
            avg_price = round(sum(prices) / len(prices))
            writer.writerow([model, avg_price, len(prices)])
        else:
            writer.writerow([model, '', 0])

print('Combined averaged prices by query saved to gpu_data_combined_avg_by_query.csv')
