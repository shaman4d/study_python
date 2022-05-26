# На вход подаётся строка из целых чисел разделённых пробелами.
# Напечатайте числа, которые больше, чем число слева от них.
# Пример ввода
# 1 5 2 4 3
# Пример вывода
# 5 4

def cc():
	prev = 0
	def compare(n):
		nonlocal prev
		r = 0
		if (prev > 0 and prev < n):
			r = n
		prev = n
		return r
	return compare
comparer = cc()

s = "1 5 2 4 3"
l = [ i for i in map(int,s.split(' ')) if comparer(i) != 0]
print(l)