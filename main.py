import requests
import validators

# Enter URL
print("Напиши URL в формате https://site.com")
url = input()

# Check correct URL

while validators.url(url) != True:
    print('Неправильный адрес')
    print("Напиши URL в формате https://site.com")
    url = input()
else:
    print('Выполняю проверку..')
    try:
        requests.get(url)
    except requests.exceptions.ConnectionError:
        print(f"Сайт {url} недоступен")

# Check domain
print('Проверка домена')
if ".ru" in url:
    print("Сайт в доменной зоне .RU")
else:
    print("Сайт в другой доменной зоне")

# Check free-date
clearUrl = url.replace("https://","")
whoisUrl = ('https://whois.ru/'+(clearUrl))
