import os
import urllib.request
import re

filename = 'dfedorov-mbox-short.txt'
if os.path.exists(filename) != True:
    print('....downloading......')
    url = 'http://dfedorov.spb.ru/python/files/mbox-short.txt'
    with urllib.request.urlopen(url) as wf:
        lines = []
        for l in wf:
            l = l.decode('utf-8')
            lines.append(l)
        with open(filename, 'w') as f:
            f.writelines(lines)

print('...parsing....')
lines = []
with open(filename) as f:
    lines = f.readlines()

emails = []
counter = 0
for l in lines:
    counter += 1
    print('line #' + str(counter))
    # match = re.search('(?P<email>\w+(?:\.*\w*)*@\w+(?:\.*\w*)*)',l)
    match = re.search('(?P<email>\w+[\.*\w*]*@\w+[\.*\w*]*)',l)
    if match is not None:
        print(match['email'])
        emails.append(match['email']+'\n')

emails = list(set(emails))

with open('dfedorov-emails.txt','w',encoding='utf-8') as f:
    f.writelines(emails)

