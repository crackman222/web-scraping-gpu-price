import requests,certifi
import os
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}

# response = requests.get('https://www.klikgalaxy.com/vga-card/?o=a&s=0',verify="C:/Users/User/Downloads/klikgalaxy.com",headers=headers)
response = requests.get('https://www.tokopedia.com/search?st=&q=nvidia%20rtx%2040&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource=',headers=headers)
# response = requests.get('https://enterkomputer.com/category/24/vga?showall=1759195954',headers=headers,verify="C:/Users/User/Downloads/enterkomputer.crt")
# print(response.status_code)
soup = BeautifulSoup(response.content, 'lxml')

save_dir = "C:/Users/User/web-scraping-gpu-price/htmlss"
os.makedirs(save_dir, exist_ok=True)
file_path = os.path.join(save_dir, "tokopedia.html")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(response.text)

# print(soup.prettify())