# Дана последовательность неотрицательных целых чисел.
# Напечатайте длину самого широкого фрагмента последовательности, где все элементы равны друг
# другу.
# Пример ввода
# 1 2 2 2 9 7 7 2 1 0
# Пример вывода
# 3

L = [1,2,2,2,9,7,7,7,7,2,1,0]

maxLength:int = 0
currLength:int = 0
prev = -1

for i in L:
	if prev == i:
		currLength += 1
	else:
		currLength = 1
	prev = i
	if currLength >=maxLength:
		maxLength = currLength
print(maxLength)