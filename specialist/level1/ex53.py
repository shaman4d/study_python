# Вводится текст одной строкой. Каждое слово разделено пробелом.
# Для каждого слова посчитайте количество данного слова встречающегося перед ним.
# Пример ввода
# one two one two three two four three
# Пример вывода
# 0 0 1 1 0 2 0 1

s = "one two one two three two four three"
l = s.split(" ")
d = {}

for i in l:
	if i in d:
		d[i] += 1
	else:
		d[i] = 0
	print(d[i])

