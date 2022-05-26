'''
На вход подаётся целое число N - количество файлов в файловой системе. Далее, подаются N строк в
формате "имя файла" и допустимые операции разделённые пробелами. Допустимые операции
следующие: W - write, R - read, X - execute. Далее, подаётся целое число М - количество операций с
файлами. Далее, подаётся М строк в формате "операция имя файла".
Напечатайте "OK", если такая операция с файлом допустима и "Denied", если нет.
Пример ввода
4
notepad.exe R X
access.log W R
logo.gif R
httpd.conf X W R
5
read logo.gif
write notepad.exe
execute logo.gif
read access.log
write access.log
Пример вывода
OK
Denied
Denied
OK
OK
'''

prg = {}

max_value = 0
with open("ex56programms.txt") as f:
	lines = f.readlines()
	for l in lines:
		prgAttr = l.strip().split(" ")
		prg[prgAttr[0]] = prgAttr[1:]

with open("ex56commands.txt") as f:
	lines = f.readlines()
	for l in lines:
		cmds = l.strip().split(' ')
		c = cmds[0]
		p = cmds[1]
		attr = prg[p]
		if c == 'read' and ('R' in attr):
			print('OK')
		elif c == 'write' and ('W' in attr):
			print('OK')
		elif c == 'execute' and ('X' in attr):
			print('OK')
		else:
			print('Denied')
