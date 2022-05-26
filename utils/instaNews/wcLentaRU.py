import wordcloud

def createNewsCloud():
	stopwordsList=None
	with open('stopwords.txt','r',encoding='utf-8') as f:
		stopwordsList = f.readline().split(',')
	stopwords = set(stopwordsList)

	lines = None
	with open("yesterdayLentaRUnews.txt","r", encoding='utf-8') as f:
		lines = f.read()


	wc = wordcloud.WordCloud(background_color='white',
						width = 800,
						height = 800,
						max_words=300,
						# mask=mask,
						stopwords=stopwords)
	wc.generate(lines)
	wc.to_file('ylrn.png')

createNewsCloud()