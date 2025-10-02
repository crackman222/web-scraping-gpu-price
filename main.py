from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# --- konfigurasi Chrome headless (tanpa UI) ---
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")

# --- jalankan browser ---
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

url = "https://www.tokopedia.com/search?st=&q=nvidia%20rtx%2040&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource="
driver.get(url)

# tunggu JS selesai render (sesuai kebutuhan)
time.sleep(3)

# --- ambil HTML hasil render ---
html = driver.page_source
soup = BeautifulSoup(html, "lxml")

# --- cari nama produk ---
nama_elem = soup.find("span", {"class": '+tnoqZhn89+NHUA43BpiJg=='})
if nama_elem:
    nama = nama_elem.get_text(strip=True)
else:
    nama = None
    print("Nama produk tidak ditemukan")

# --- cari harga produk ---
harga_elem = soup.find("span", {"class": 'urMOIDHH7I0Iy1Dv2oFaNw=='})
if harga_elem:
    harga = harga_elem.get_text(strip=True)
else:
    harga = None
    print("Harga produk tidak ditemukan")

print("Nama:", nama)
print("Harga:", harga)

driver.quit()
