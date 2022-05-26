import json

print('Open RU locale...')
fileRU = open('RU_mobile.json', encoding='utf-8')

print('Processing RU locale...')
dataRU = json.load(fileRU)
dataRUKeys = dataRU["keys"]

# print(dataRU["keys"]["panel_achs_title"])

print('Open EN locale...')
fileEN = open('EN_web.json')

result = ''

enLines = fileEN.readlines()
for l in enLines:
	line = l
	if line.find('{') !=-1 or \
		line.find('}') !=-1 or \
		line.find('"id"')!=-1 or \
		line.find('"keys"')!=-1:
		pass
	elif line.strip() == '':
		# pass empty lines or lines with some control symbols like \t \n
		pass
	else:
		lineParts = line.split(':')
		# searching for quotes
		# extracting key
		keyStartQidx = lineParts[0].find('"')
		keyEndQidx = lineParts[0].find('"',keyStartQidx+1)
		originalKey = lineParts[0][keyStartQidx+1:keyEndQidx]
		translation = ''
		if originalKey in dataRUKeys:
			translation = dataRUKeys[originalKey]
			# print(translation)

		# extracting content
		contentStartQidx = lineParts[1].find('"')
		contentEndQidx = lineParts[1].find('"',contentStartQidx+1)
		originalContent = lineParts[1][contentStartQidx+1:contentEndQidx]
		afterContentPart = lineParts[1][contentEndQidx:]
		# print(contentStartQidx, contentEndQidx, originalContent, afterContentPart)
		if translation != '':
			if originalContent != '':
				line = line.replace(originalContent, translation)
			else:
				line = lineParts[0] + ': "' + translation + afterContentPart;
		else:
			line = line.replace(originalContent, '@'+originalContent+'@')
	result += line
	
# print(result)
print('Conversion completed.')

convertedRU = open('RU_web.json', 'w', encoding='utf-8')
convertedRU.write(result)

fileRU.close()
fileEN.close()
convertedRU.close()
	
