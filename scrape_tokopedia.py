import requests,certifi
import os
from bs4 import BeautifulSoup
import csv
from urllib.parse import quote

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}
queries = ["rtx 2060","rtx 2070","rtx 2080", 
           "rtx 3050", "rtx 3060", "rtx 3070", "rtx 3080", "rtx 3090", 
           "rtx 4060", "rtx 4070", "rtx 4080", "rtx 4090",
           "rtx 5050", "rtx 5060", "rtx 5070", "rtx 5080", "rtx 5090"]

with open("gpu_data_toped.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Nama", "Harga", "Toko", "Query"])  # header CSV

    for q in queries:
        query_encoded = quote(q) 
        url = f"https://www.tokopedia.com/search?st=&q={query_encoded}"   
    
        print(f"Scraping: {q}")
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.content, 'lxml')

        # Loop tiap produk
        for product in soup.find_all("div", class_="gG1uA844gIiB2+C3QWiaKA=="): 
            name_elem = product.find("span", class_="+tnoqZhn89+NHUA43BpiJg==")
            price_elem = product.find("div", class_="urMOIDHH7I0Iy1Dv2oFaNw==")
            shop_elem = product.find("span", class_="si3CNdiG8AR0EaXvf6bFbQ==")

            name = name_elem.get_text(strip=True) if name_elem else ""
            price = price_elem.get_text(strip=True) if price_elem else ""
            shop = shop_elem.get_text(strip=True) if shop_elem else ""

            writer.writerow([name, price, shop, q])

# save_dir = "C:/Users/User/web-scraping-gpu-price/htmlss"
# os.makedirs(save_dir, exist_ok=True)
# file_path = os.path.join(save_dir, "tokopedia.html")

# with open(file_path, "w", encoding="utf-8") as f:
#     f.write(response.text)

# print(soup.prettify())