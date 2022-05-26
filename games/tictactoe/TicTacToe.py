import random


def printBoard(board, playerChips):
	boardp = [playerChips[i] for i in board]
	print(' '+boardp[7]+' | '+boardp[8]+' | '+boardp[9]+' ')
	print('---+---+---')
	print(' '+boardp[4]+' | '+boardp[5]+' | '+boardp[6]+' ')
	print('---+---+---')
	print(' '+boardp[1]+' | '+boardp[2]+' | '+boardp[3]+' ')
	pass

def isTie(board):
	if board[1] != 0 and board[2] != 0 and board[3] != 0 and \
		board[4] != 0 and board[5] != 0 and board[6] != 0 and \
			board[7] != 0 and board[8] != 0 and board[9] != 0:
			return True
	return False 
	
def isWinOnBoard(board, value):
	if board[1] == board[2] == board[3] == value: return True
	if board[4] == board[5] == board[6] == value: return True
	if board[7] == board[8] == board[9] == value: return True
	
	if board[1] == board[4] == board[7] == value: return True
	if board[2] == board[5] == board[8] == value: return True
	if board[3] == board[6] == board[9] == value: return True
	
	if board[1] == board[5] == board[9] == value: return True
	if board[3] == board[5] == board[7] == value: return True

	return False
	
def getWinMove(board, value):
	for i in range(1, len(board)):
		b = board[:]
		if b[i] == 0:
			b[i] = value
			if isWinOnBoard(b, value):
				return i
	return 0

def getCornerMove(board, value):
	if board[1] == 0: return 1
	if board[3] == 0: return 3
	if board[7] == 0: return 7
	if board[9] == 0: return 9
	return 0
			
def getCenterMove(board, value):
	if board[5] == 0: return 5
	return 0
			
def getCrossMove(board, value):
	if board[2] == 0: return 2
	if board[4] == 0: return 4
	if board[6] == 0: return 6
	if board[8] == 0: return 8
	return 0

print('========================================================')
print('               игра КРЕСТИКИ-НОЛИКИ игра')
print('========================================================')
print('У вас есть игровое поле 3х3.')
print('В свой ход вы можете ставить свой крестик(нолик) в одну из')
print('пронумерованных ячеек:')
print(' 7 | 8 | 9 ')
print('---+---+---')
print(' 4 | 5 | 6 ')
print('---+---+---')
print(' 1 | 2 | 3 ')
print('Выиграть можно поставив свои крестики(или нолики) 3 в ряд,')
print('по вертикали, горизонтали или диагонали.')
while True:
	# user choose 
	userChoise = ''
	while userChoise == '':
		print('Вы будете играть крестиками "x" или ноликами "o"')
		userChoise = input().strip().lower()[0]
		if userChoise.find('x') == -1 and userChoise.find('o') == -1:
			userChoise = ''
	if userChoise == 'x':
		playersChips = [' ','X','O']
	else:
		playersChips = [' ','O','X']
	print('Первым будет ходить....')
	isHumanMove = True
	# coin = random.randint(0,1)
	# if coin == 1:
		# isHumanMove = False
	print("Вы!" if isHumanMove == True else "Компьютер")
	isGamePlaying = True

	board = [0,0,0,0,0,0,0,0,0,0]

	while isGamePlaying:
		printBoard(board, playersChips)
		
		if isTie(board) == True:
			print(".............................")
			print("            Ничья...")
			print(".............................")
			isGamePlaying = False

		if isHumanMove == True:
			cell = ''
			while cell == '':
				cell = input('\nКуда будете ставить свой '+playersChips[1]+'(введите номер клетки)?')
				if cell.isdigit():
					cellNum = int(cell[0])
					if board[cellNum] != 0:
						print('Эта ячейка уже занята!')
						cell = ''
					else:
						board[cellNum] = 1
				else:
					cell = ''
			
			if isWinOnBoard(board,1):
				printBoard(board, playersChips)
				print("=============================")
				print("   Ура! Вы выиграли ! ! !")
				print("=============================")
				isGamePlaying = False
			else:
				isHumanMove = False
		else:
			print("\nХод компьютера:")
			pcMove = 0
			# get possible win move
			pcMove = getWinMove(board,2)
			if pcMove == 0:
				# get possible opponent win move to block it
				pcMove = getWinMove(board,1)
			if pcMove == 0:
				# get possible move in one of four corners
				pcMove = getCornerMove(board,2)
			if pcMove == 0:
				# get possible move in the center
				pcMove = getCenterMove(board,2)
			if pcMove == 0:
				# get possible move in one of vertical and horizontal cells
				pcMove = getCrossMove(board,2)
			
			board[pcMove] = 2
			if isWinOnBoard(board,2):
				printBoard(board, playersChips)
				if isHumanMove == False:
					print("=============================")
					print("   Я компьютер! И я выиграл!")
					print("          ХА - ХА - ХА")
					print("=============================")
				isGamePlaying = False
			else:
				isHumanMove = True
			isHumanMove = True
	answer = ''
	while answer == '':
		answer = input('Хотите еще сыграть (y/n)?')
		if answer == 'y':
			continue
		else:
			break