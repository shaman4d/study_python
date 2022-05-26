import requests

ttt = requests.get(
    'https://export.yandex.ru/bar/reginfo.xml?region=231')

with open('moscow_weather.xml', 'wb') as f:
    f.write(ttt.content)
