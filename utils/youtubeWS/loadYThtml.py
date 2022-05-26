import requests

responce = requests.get('https://www.youtube.com/results?search_query=%D0%BC%D0%B0%D0%B9%D0%B4%D0%B0%D0%BD')

with open('yt.html','wb') as f:
	f.write(responce.content)