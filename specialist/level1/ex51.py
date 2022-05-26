# На вход подаётся строка, в которой несколько раз встречается вхождение буквы "h".
# Напечатайте эту строку так, чтобы символы между первым и последним вхождением буквы "h" шли в
# обратном порядке.
# Пример ввода
# In the hole in the ground there lived a hobbit
# Пример вывода
# In th a devil ereht dnuorg eht ni eloh ehobbit

s = "In the hole in the ground there lived a hobbit"

print(s[:s.index('h')+1] + s[len(s)-(s[::-1].index('h')+2):s.index('h')-1:-1] + s[len(s)-(s[::-1].index('h')):len(s)])