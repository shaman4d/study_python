import wikipedia
import wordcloud
import numpy as np 
from PIL import Image


def getWiki(query):
	title = wikipedia.search(query)[0]
	page = wikipedia.page(title)
	return (title,page.content)

def colorizer(word, font_size, position,orientation,random_state=None, **kwargs):
    # return("hsl(230,100%%, %d%%)" % np.random.randint(49,51))
    return("rgb({},{},0)".format(font_size*3 + 50, len(word) + 10))

def createWordcloud(wikiArticle):

	stopwords = set(wordcloud.STOPWORDS)

	mask = np.array(Image.open('mask_lenin.png'))

	wc = wordcloud.WordCloud(background_color='white',
						width = 1200,
						height = 1200,
						max_words=300,
						# mask=mask,
						stopwords=stopwords)
	wc.generate(wikiArticle[1])
	# wc.recolor(color_func=colorizer)
	wc.to_file('{}.png'.format(wikiArticle[0]))

# createWordcloud(getWiki('Java_(programming_language)'))
createWordcloud(getWiki('c language'))
