'''
Игра Виселица
'''
# 			data definitions
HANGMANS = [
	'''
    +---+
        |
        |
        |
        |
  _____===__
	''',
	'''
    +---+
    o   |
        |
        |
        |
  _____===__
	''',
	'''
    +---+
    o   |
    |   |
        |
        |
  _____===__
	''',
	'''
    +---+
    o   |
   /|   |
        |
        |
  _____===__
	''',
	'''
    +---+
    o   |
   /|\  |
        |
        |
  _____===__
	''',
	'''
    +---+
    o   |
   /|\  |
    |   |
        |
  _____===__
	''',
	'''
    +---+
    o   |
   /|\  |
    |   |
   /    |
  _____===__
	''',
	'''
    +---+
    o   |
   /|\  |
    |   |
   / \  |
  _____===__
	'''
]

WORDS = ['квартал','олень','барсук','хипстер','зрение','программирование','власть','честность','президент','правило','аккордион','гармошка','медведь',
'колесо','огонь','дерево','телега','чума','красота','радуга','месть','жилище','варан','ворон','капуста','площадь','картошка','герой','квазар',
'пушка','центр','столица','гвардия','тригонометрия','понимание','математика']

#------------------------------------------------------------------------------------------------------------------
def showCurrentState():
	print("\n")
	print(HANGMANS[currTry])
	l = [ (currWord[i] + ' ') if currLetters[i] == 1 else '_ ' for i in range(0,len(currWord))]
	print('СЛОВО: ',''.join(l))

def askLetter():
	needToAsk = True
	while needToAsk:
		global letter
		letter = input('Ваша буква? ').lower()
		if letter.isdigit():
			print('Ошибка: вы ввели число.')
		else:
			needToAsk = False

def analyzeLetter():
	global letter
	global currWord
	global playerWon
	winCounter = 0
	letter = letter[0]
	guessLetter = False
	for i in range(0, len(currWord)):
		if letter == currWord[i]:
			currLetters[i] = 1
			guessLetter = True
		if currLetters[i] == 1:
			winCounter += 1
	if guessLetter == False:
		global currTry
		currTry += 1
	if winCounter == len(currWord):
		playerWon = True

def analyzeWin():
	global gameIsPlaying
	if playerWon == True:
		gameIsPlaying = False
		print('================================')
		print('        слово:', currWord)
		print('')
		print('        ВЫ МОЛОДЕЦ ! ! !')
		print('        ВЫ ВЫИГРАЛИ ! ! !')
		print('================================')
	else:
		global currTry
		if currTry == len(HANGMANS):
			gameIsPlaying = False
			print('----------------------------------')
			print('    К сожалению вы проиграли...')
			print('----------------------------------')

#------------------------------------------------------------------------------------------------------------------
import random

gameIsPlaying = True
playerWon = False

currWord = WORDS[random.randint(0, len(WORDS)-1)]
currLetters = [0 for i in currWord]
currTry = 0
letter = ''

print("-------------------------------------------------------------------------")
print("                  игра    В И С Е Л И Ц А   игра")
print("-------------------------------------------------------------------------")
print("   Компьютер загадывает слово и у вас есть 7 попыток его разгадать.      ")
print("-------------------------------------------------------------------------")


# main game loop
while gameIsPlaying:
	showCurrentState()
	askLetter()
	analyzeLetter()
	analyzeWin()
