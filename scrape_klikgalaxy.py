import requests,certifi
import os
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}
base = "https://www.klikgalaxy.com"
url = "https://www.klikgalaxy.com/vga-card/?o=a&s=0"

with open("gpu_data_kgal.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Nama", "Harga", "Toko"])  # header CSV
    while url:
        response = requests.get(url,verify="C:/Users/ideapad/Downloads/klikgalaxy.crt",headers=headers)
        # response = requests.get('https://www.tokopedia.com/search?st=&q=nvidia%20rtx%2040&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource=',headers=headers)
        # response = requests.get('https://enterkomputer.com/category/24/vga?showall=1759195954',headers=headers,verify="C:/Users/User/Downloads/enterkomputer.crt")
        # print(response.status_code)
        soup = BeautifulSoup(response.content, 'lxml')

        name_selector = ".product-title-column"
        price_selector = ".product-price"
        # shop_selector = "klikgalaxy"



        # Loop tiap produk
        for product in soup.select("td.hotitems"):  # ganti selector container sesuai HTML
            name_elem = product.select_one(name_selector)
            price_elem = product.select_one(price_selector)
            # shop_elem = product.select_one(shop_selector)

            name = name_elem.get_text(strip=True) if name_elem else ""
            price = price_elem.get_text(strip=True) if price_elem else ""
            # toko = toko_elem.get_text(strip=True) if toko_elem else ""
            shop = "klikgalaxy"

            writer.writerow([name, price, shop])
        # next page
        next = soup.find("a", string=lambda t: t and "next" in t.lower())
        if next:
            href = next["href"]

            if href.startswith("/"):
                href = base + href
            url = href
        else:
            url = None


# save_dir = "C:/Users/User/web-scraping-gpu-price/htmlss"
# os.makedirs(save_dir, exist_ok=True)
# file_path = os.path.join(save_dir, "tokopedia.html")

# with open(file_path, "w", encoding="utf-8") as f:
#     f.write(response.text)

# print(soup.prettify())