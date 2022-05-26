import requests
import pandas as pd

numberOfPages = 100

jobs = ['Python','HTML']

for job in jobs:
	data = []
	for i in range(numberOfPages):
		print(f'...page:{i}...')
		url = 'https://api.hh.ru/vacancies'
		par = {'text': {job}, 'area':'113','per_page':10, 'page':i}
		r = requests.get(url, params=par)
		if r.status_code == 200:
			print('OK')
		else:
			print('...something went wrong...')
			continue
		data.append(r.json())
	vacancyDetails = data[0]['items'][0].keys()
	df = pd.DataFrame(columns=list(vacancyDetails))
	ind = 0
	for i in range(len(data)):
		for j in range(len(data[i]['items'])):
			df.loc[ind] = data[i]['items'][j]
			ind += 1
	csvName = job+'.csv'
	df.to_csv(csvName)