# На вход подаётся целое число N - количество записей в словаре. Далее подаются N пар: фамилия
# кандидата в президенты и число проголосовавших.
# Задача посчитать и вывести фамилии кандидатов с общим числом, которое они набрали. Фамилии
# вывести в алфавитном порядке.
# Пример ввода
# Smith 10
# Smith 5
# Dow 9
# Dow 8
# Smith 1
# Пример вывода
# Dow 17
# Smith 16

d = {}
with open("ex54file.txt") as f:
	lines = f.readlines();
	for l in lines:
		candList = l.split(" ")
		if candList[0] in d:
			d[candList[0]] += int(candList[1])
		else:
			d[candList[0]] = int(candList[1])

lkeys = list(d.keys());
lkeys.sort()
for i in lkeys:
	print(i, d[i])
