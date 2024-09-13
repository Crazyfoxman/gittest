import requests
from bs4 import BeautifulSoup

link = 'https://browser-info.ru'

parshtml = requests.get(link).text
answer = BeautifulSoup(parshtml, 'lxml')
soup = answer.find('div', id='tool_padding')
flash = soup.find('div', id='flash_version')
status = flash.find_all('span')[1].text
print(status)