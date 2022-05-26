import os
import urllib.request
import re

filename = 'dfedorov-abzatz.txt'
if os.path.exists(filename) != True:
    print('....downloading......')
    url = 'http://dfedorov.spb.ru/python/files/p.html'
    with urllib.request.urlopen(url) as wf:
        lines = []
        for l in wf:
            l = l.decode('utf-8')
            lines.append(l)
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(lines)

print('...parsing....')
lines = []
with open(filename, encoding='utf-8') as f:
    lines = f.readlines()


counter = 0
txtlines = []
for l in lines:
    counter += 1
    print('line #' + str(counter) + l)

    l = re.sub('<.+>', '', l).strip()
    if len(l) > 0:
        print(l)
        txtlines.append(l)



with open('dfedorov-abzatz-result.txt','w',encoding='utf-8') as f:
    f.writelines(txtlines)


