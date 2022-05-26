import os
import re
import urllib.request as ureq
import requests
from clint.textui import progress

print('---------- Pushnoy songs downloader -----------')

storageUrl = 'http://www.files.pushnoy.ru/tut/'

lines = []
if os.path.exists('data.txt') != True:
    print('...download page...')
    with ureq.urlopen(storageUrl) as storagePage:
        for line in storagePage:
            line = line.decode('cp1251').strip()
            lines.append(line + '\n')
        with open('data.txt', mode='w', encoding='utf-8') as f:
            f.writelines(lines)
else:
    with open('data.txt', encoding='utf-8') as f:
        lines = f.readlines()


ch_size = 1024 * 1024
print('...extracting URLs...')
mp3urls = {}
for l in lines:
    # print(l.strip())
    match = re.search('<A HREF=\"(?P<mp3url>.*?\.mp3)\">',l)
    if match is not None:
        url = match['mp3url']
        mp3urls[url] = storageUrl + '/' + match['mp3url']
        #print(url, mp3urls[url])


#------------------------------------------------------------------
print('................loading music..............')
counter = 0
for k in mp3urls:
    print('\nloading:' + mp3urls[k])
    r = requests.get(mp3urls[k], stream=True)
    with open('songs/'+k, 'wb') as fsong:
        total_length = int(r.headers.get('content-length'))
        '''
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                fsong.write(chunk)
        '''
        for chunk in progress.bar(r.iter_content(chunk_size=ch_size), expected_size=(total_length/ch_size)+1, label='Length:' + str(total_length)):
            if chunk:
                fsong.write(chunk)







