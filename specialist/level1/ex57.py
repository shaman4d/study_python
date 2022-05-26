'''
На вход подаётся целое число N - количество строк подаваемых на вход. Далее, подаются N строк в
формате "страна город город ...". Далее, на вход подаётся целое число М - количество следующих
подаваемых строк. Далее, M городов.
Для каждого переданного города напечатайте страну, в которой он находится.
Пример ввода
2
USA Boston Pittsburgh Washington Seattle
UK London Edinburgh Cardiff Belfast
3
Cardiff
Seattle
London
Пример вывода
UK
USA
UK
'''

placeDefOccured:bool = False
citiesOccured:bool = False

places = {}


with open('ex57file.txt') as f:
	lines = f.readlines()
	for l in lines:
		tokens = l.strip().split(' ')
		if tokens[0].isdigit():
			if placeDefOccured != True:
				placeDefOccured = True
			else:
				citiesOccured = True
		else:
			if placeDefOccured == True and citiesOccured != True:
				places[tokens[0]] = tokens[1:]
			else:
				for i in places:
					if tokens[0] in i:
						print(i)
						break