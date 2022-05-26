import urllib.request as ur

url = "http://dfedorov.spb.ru/python3/src/romeo.txt"

with ur.urlopen(url) as webpage:
	for line in webpage:
		line = line.strip().decode('utf-8')
		print(line)