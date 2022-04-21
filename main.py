from ctypes.wintypes import PINT
import requests
import whois
import validators
from bs4 import BeautifulSoup


# Enter URL
print("Напиши URL в формате https://site.com")
url = input()

# Check correct URL
while validators.url(url) != True:
    print('Неправильный адрес')
    print("Напиши URL в формате https://site.com")
    url = input()
else:
    print('Выполняю проверку..'+'\n')
    try:
        requests.get(url)
    except requests.exceptions.ConnectionError:
        print(f"Сайт {url} недоступен")

# Check domain
print('Проверка домена')
if ".ru" in url:
    print("Сайт в доменной зоне .RU"+'\n')
else:
    print("Сайт в другой доменной зоне"+'\n')

# Check free-date
clearUrl = url.replace("https://","")
whoisData = whois.whois(clearUrl)

#print(whoisData)


expDate = whoisData["expiration_date"]
org = str(whoisData["org"])
print('Дата окончания домена: '+str(expDate))

if org == 'None':
    print('В хуиз домена закрытая информация')
else:
    print('Организация: '+str(org))
