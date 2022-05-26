sportDict = {}

def addSport(sport):
    sport = sport.strip().lower()
    if len(sport) > 0 and sport.isalpha():
        if sport not in sportDict:
            sportDict[sport] = 1
        else:
            sportDict[sport] += 1


with open('sport.txt', encoding='cp1251') as f:
    lines = f.readlines()

for l in lines:
    tokens = l.split('\t')
    if len(tokens) >= 4:
        sport = tokens[3].strip()
        if sport.find(',') != -1:
            sports = sport.split(',')
            for i in sports:
                addSport(i)
        else:
            addSport(sport)
    print(tokens)

for k in sorted(sportDict):
    print(k + ' ' + str(sportDict[k]))
