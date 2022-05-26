import time
import requests
import re
from calendar import monthrange

def getDailyNews(year, month, day):
	news = []
	news_dict = {}
	for hour in [24,20,16,12,8,4]:
	# for hour in [24]:
		ts = int(time.mktime((year,month,day,hour,0,0,0,0,0)))
		print(f"{hour} - {ts}")
		url =f"https://m.lenta.ru/parts/news/?after={ts}"
		result = requests.get(url, headers={"X-Requested-With":"XMLHttpRequest"})
		result.encoding = "utf-8"
		newsTime = re.findall(r'datetime="\s(\d+:\d+),', result.text)
		newsUrls = re.findall(r'<a.*?href="(.*?)"', result.text)
		newsTitles = re.findall(r'<span class=\"b-list-item__title\">(.*?)</span>', result.text)
		for i in range(len(newsTime)):
			if 'http' in newsUrls[i]: continue
			news_dict[newsTime[i]] = [newsTime[i], newsTitles[i], newsUrls[i]]
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
		fileName = 'lentaRUnews/' + last_value[2][6:-1].replace('/','_') + '.txt'
		with open(fileName,'w', encoding='utf-8') as f:
			f.write(last_value[1])
			f.write('\n')
			f.write(news_page_content)
	time.sleep(0.5)

def mineNewsSince(year=2019, endYear=2019, month=10, day=3):
	now_ts = int(time.time())
	endYear = endYear
	currYear = year
	currMonth = month
	endDateReached = False

	while currYear <= endYear and endDateReached != True:
			currDay = day
			endDay = monthrange(currYear, currMonth)[1]
			while currDay <= endDay:
				# check limit of current date
				if time.mktime((currYear,currMonth,currDay,0,0,0,0,0,0)) > now_ts:
					endDateReached = True
					break
				print(f"d{currDay} m{currMonth} y{currYear}")
				getDailyNews(currYear, currMonth, currDay)
				currDay+=1
			currMonth+=1
			if currMonth>12: currYear+=1
	pass

# getDailyNews(2019,10,3)

mineNewsSince(2019,2019,7,23)