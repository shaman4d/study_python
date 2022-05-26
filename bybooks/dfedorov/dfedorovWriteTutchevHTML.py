import urllib.request

url = ' http://dfedorov.spb.ru/python/files/tutchev.txt'

page = '''
<!DOCTYPE html>
<html>
    <head>
       <meta charset="utf-8">
       <title>Стих Тютчева</title>
    </head>
    <body>
'''
counter = 0
with urllib.request.urlopen(url) as wp:
    for l in wp:
        l = l.strip().decode('utf-8');
        if counter == 0:
            page += '<p>'+ l +'</p>'
        else:
            if len(l) > 0:
                page += l + '<br>'
        counter += 1
page += '<p>' + '<img src="http://dfedorov.spb.ru/python/files/tutchev.jpg"/>'

page += '</body></html>'

with open('tutchev.html','w', encoding='utf-8') as f:
    f.write(page)
