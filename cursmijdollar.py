import requests
from bs4 import BeautifulSoup as BS
import lxml

url = 'https://finance.ua/'
r = requests.get(url)
soup = BS(r.text, 'lxml')

cursmijdollar = soup.find(class_="fua-xrates__index").findParent()

for item in cursmijdollar:
    print(item.text.strip())
