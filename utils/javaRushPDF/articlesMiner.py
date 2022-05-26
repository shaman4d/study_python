import requests

# https://javarush.ru/groups/posts?order=OLD
# GET /api/1.0/rest/posts?order=OLD&filter=ALL&offset=12&limit=12 HTTP/1.1

# getting all articles data

# MAX_ARTICLES_NUM = 2200
# LOADING_ARTICLE_STEP = 50
MAX_ARTICLES_NUM = 20
LOADING_ARTICLE_STEP = 10

counter = 0
for i in range(0,MAX_ARTICLES_NUM,LOADING_ARTICLE_STEP):
	resp = requests.get(f'https://javarush.ru//api/1.0/rest/posts?order=OLD&filter=ALL&offset={i}&limit={LOADING_ARTICLE_STEP}')
	articles = resp.json()
	for a in articles:
		print(a['id'], a['key'])
		counter += 1
		# with open('articles/a'+str(counter)+'.html', 'w', encoding='utf-8') as f:
		with open('articles/a'+str(counter)+'.html', 'w', encoding='utf-8') as f:
			f.write('<h1>' + a['title'] + '</h1>' + a['content'])