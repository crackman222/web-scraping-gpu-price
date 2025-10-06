import csv

# Dictionary to store prices by query
model_prices = {}

with open('gpu_data_toped.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        query = row.get('Query', '').strip()
        price_str = row.get('Harga', '').replace('Rp', '').replace('.', '').replace(',', '').strip()
        try:
            price = int(price_str)
        except:
            continue
        if query:
            if query not in model_prices:
                model_prices[query] = []
            model_prices[query].append(price)

# Output average prices
with open('gpu_data_toped_avg_by_query.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Model (Query)', 'Average Price (IDR)', 'Sample Size'])
    for model, prices in model_prices.items():
        if prices:
            avg_price = round(sum(prices) / len(prices))
            writer.writerow([model, avg_price, len(prices)])
        else:
            writer.writerow([model, '', 0])

print('Averaged prices by query saved to gpu_data_toped_avg_by_query.csv')
