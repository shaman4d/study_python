# Даны две метки времени одного дня. Метка времени состоит из полного количества часов, минут и
# секунд, например: 1 15 23 - один час 15 минут и 23 секунды. Первая метка времени произошла
# раньше второй.
h0 = int(input("?"))
m0 = int(input("?"))
s0 = int(input("?"))
h1 = int(input("?"))
m1 = int(input("?"))
s1 = int(input("?"))
print( (h1 * 60 * 60 + m1 * 60 + s1) - (h0 * 60 * 60 + m0 * 60 + s0 ) )