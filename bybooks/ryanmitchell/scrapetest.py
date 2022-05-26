# from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

# html = urlopen('http://pythonscraping.com/pages/page1.html')
html = requests.get('http://pythonscraping.com/pages/page1.html')
# bsObj = BeautifulSoup(html.read(), features='html.parser')
bsObj = BeautifulSoup(html.content, features='html.parser')
print(bsObj.h1)
