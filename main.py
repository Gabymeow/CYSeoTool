from asyncio.windows_events import NULL
from ctypes.wintypes import PINT
import requests
import whois
import validators
import re
import json
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

# Org check (нужна проверка на то, когда нет ORG)
if org == 'None':
    print('В хуиз домена закрытая информация'+'\n')
else:
    print('Организация: '+str(org)+'\n')

# geo name check (Надо расширить спиоск или как-то иначе проверять)
geoNames = ['spb','msk']
geo = bool(re.search('spb', clearUrl))
if geo == True:
    print('Есть указание на географию в домене'+'\n')
else:
    print('geo clear'+'\n')

#subdomens check be1 API
be1ApiKey = 'm0xomKo92U6Zeo9JhlqSHEyMxygW0u0K'
tool = 'uznat-poddomeni-saita'

be1ApiCon = requests.post('https://be1.ru/api/tools/add-task?apikey='+be1ApiKey, data={'tool':'uznat-poddomeni-saita', 'domain':clearUrl})

print('Ищу доступные поддомены..'+'\n')
if be1ApiCon.status_code == 200:
    print('Success!')
elif be1ApiCon.status_code == 404:
    print('Not Found.')
print (be1ApiCon.json()['message'])