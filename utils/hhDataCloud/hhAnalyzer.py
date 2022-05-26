import pandas as pd
import json
import re
import collections
from wordcloud import WordCloud, STOPWORDS

fname ='Python'
df = pd.read_csv(f'{fname}.csv')
df.rename(columns={'Unnamed: 0':'index'}, inplace=True)
df.set_index('index', inplace=True)


vacancy_names = df.name
salary = df.salary
snippet = df.snippet

mystopwords = set(['<','>','highlighttext','senior','старший','специалист','риски','stack','customer','продажам','на','больших','trip','year'])

# stopwords = set(STOPWORDS)
stopwords = mystopwords

cloud = ''

def procVac():
     global cloud
     for x in list(vacancy_names):
          cloud += x + ' '

def procSalary():
     global cloud
     patt = re.compile('\d+')
     for x in list(salary):
          if isinstance(x, str) and 'from' in x:
               match = patt.search(x)
               cloud += match.group() + 'руб. '

def procReqs():
     global cloud
     patt = re.compile(".*requirement\W*(.*)',")
     for x in list(snippet):
          if isinstance(x, str) and 'requirement' in x:
               match = patt.search(x)
               if match is not None:
                    cloud += match.group(1) + ' '

procFlow = [['vacancies',procVac],['salary',procSalary],['reqs',procReqs]]

for flow in procFlow:
     cloud =''
     flow[1]()
     wordcloud = WordCloud(width = 1000, height = 1000, 
                              stopwords = stopwords, 
                              max_words=500,
                              min_font_size = 8,background_color='white'
                         ).generate(cloud)

     wordcloud.to_file('{}_{}.png'.format(fname, flow[0]))