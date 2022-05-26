'''
На вход подаются N строк из слов. Если несколько слов в строке, они разделяются пробелом.
Для каждого слова напечатайте его количество. Список слов выведите по частоте.

Пример ввода
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme

Пример вывода
damme 4
is 3
name 3
van 3
bond 2
claude 2
hi 2
my 2
james 1
jean 1
what 1
your 1
'''
d = {}
with open("ex58file.txt") as f:
	lines = f.readlines()
	for l in lines:
		tokens = l.strip().split(' ')
		for t in tokens:
			if t in d:
				d[t] += 1
			else:
				d[t] = 1
l = sorted(d.items(), key=lambda x:x[1], reverse=True)
for i in l:
	print(i[0], i[1])