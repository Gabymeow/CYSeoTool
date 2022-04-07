import requests
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
whoisUrl = requests.get('https://whois.ru/'+(clearUrl))

soup = BeautifulSoup(whoisUrl.content, 'html.parser')
text = soup.find_all(class_="raw-domain-info-pre")
print('Информация о домене: '+(str(text[1]))+ '\n')

# Check HTML sitemap
print('Поиск HTML карты сайта: ')
HTMLSitemap = ['map', 'sitemap', 'karta']

for tail in HTMLSitemap:
    mapURL = requests.get(url+'/'+tail)
    if mapURL.status_code == 200:
        print('Найдена карта сайта' + '\n')
        break

# Check style <body>
#styleUrl = requests.get(url)
#soup1 = BeautifulSoup(styleUrl.content, 'html.parser')
#style = soup1.find_all('body')
#print (style)