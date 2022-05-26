a=10
b=100
try:
	y = a/b
	print('hoho' + y)
except ZeroDivisionError:
	print('tried divide by zero')
except TypeError:
	print('u dumb')
else:
	print(y)

print('!!!!!!!............')	
