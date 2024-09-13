import requests
from bs4 import BeautifulSoup

link = "https://browser-info.ru"

html_code = requests.get(link).text
soup = BeautifulSoup(html_code, "lxml")
block = soup.find('div', id="tool_padding")
cookie = block.find('div', id="cookie_check")
status = cookie.find_all('span')[1].text

print(status)