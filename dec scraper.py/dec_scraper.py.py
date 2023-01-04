from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil

url = "https://rubikscode.net/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

aas = soup.find_all("a", class_='entry-featured-image-url')

image_info = []

for a in aas:
    image_tag = a.findChildren("img")
    image_info.append((image_tag[0]["src"], image_tag[0]["alt"]))

print(soup)