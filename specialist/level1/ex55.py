# Далее, подаётся N строк слов, которые разделены пробелами.
# Напечатайте слово, которое встречается в строках наибольшее количество раз. Если таких слов
# несколько, то напечатайте то слово, которое стоит раньше других в алфавитном порядке.
# 
# Пример ввода
# apple orange banana
# banana orange
# 
# Пример вывода
# banana

d = {}
max_value = 0
with open("ex55file.txt") as f:
	lines = f.readlines()
	for l in lines:
		words = l.strip().split(' ')
		for w in words:
			if w in d:
				d[w] += 1
			else:
				d[w] = 1
			if max_value < d[w]: max_value = d[w]

l = sorted(d.items(), key=lambda x :x[0])

for i in l:
	if i[1] == max_value:
		print(i[0], i[1])
		break
