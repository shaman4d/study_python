import re

with open("tmp.css", 'r') as f:
	content = f.read()



# result = re.search('fact',content)
# print(result.group())
results = re.search('fact__theme_day-clear:before\s*{.*?url\((?P<ulink>.*?)\)', content)
print(results.group('ulink'))
# for r in results:
	# print('---------')
	# print(r)