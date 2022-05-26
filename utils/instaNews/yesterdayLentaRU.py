import time
import requests
import re
from datetime import date, timedelta
from calendar import monthrange

def getDailyNews(year, month, day):
	news = []
	news_dict = {}
	for hour in [24,20,16,12,8,4]:
		ts = int(time.mktime((year,month,day,hour,0,0,0,0,0)))
		print(f"{hour} - {ts}")
		url =f"https://m.lenta.ru/parts/news/?after={ts}"
		result = requests.get(url, headers={"X-Requested-With":"XMLHttpRequest"})
		result.encoding = "utf-8"
		newsTime = re.findall(r'datetime="\s(\d+:\d+),', result.text)
		newsUrls = re.findall(r'<a.*?href="(.*?)"', result.text)
		newsTitles = re.findall(r'<span class=\"b-list-item__title\">(.*?)</span>', result.text)
		previousHour = 999
		currHour = previousHour
		for i in range(len(newsTime)):
			if 'http' in newsUrls[i]: continue
			currHour = int(newsTime[i].split(':')[0])
			if  currHour > previousHour: break
			previousHour = currHour 
			news_dict[newsTime[i]] = [newsTime[i], newsTitles[i], newsUrls[i]]

	fileName = 'yesterdayLentaRUnews.txt'
	with open(fileName,'w', encoding='utf-8') as f:
		for k,v in news_dict.items():
			print("{} {} : {}".format(v[0], v[1], v[2]))
			last_value = v
			news_page = requests.get('https://m.lenta.ru' + last_value[2])
			news_page.encoding = 'utf-8'
			news_page_content = re.findall(r'<div class=\"b-topic__body\".*?>(.*)</p><div',news_page.text)
			if len(news_page_content) == 0: continue
			news_page_content = news_page_content[0]
			news_page_content = re.sub(r'<aside.*?</aside>','',news_page_content)
			news_page_content = re.sub(r'<.*?>','',news_page_content)
			f.write(last_value[1])
			f.write('\n')
			f.write(news_page_content)
			f.write('\n\n')

today = date.today()
yesterday = today - timedelta(days=1)
print("{} {} {}".format(yesterday.year, yesterday.month, yesterday.day))
getDailyNews(yesterday.year, yesterday.month, yesterday.day)