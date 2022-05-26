# На вход подаётся строка, в которой несколько раз встречается вхождение буквы "h".
# Напечатайте эту строку предварительно удалив из неё первое и последнее вхождение буквы "h", а
# также все символы между ними.
# Пример ввода
# In the hole in the ground there lived a hobbit
# Пример вывода
# In tobbit

s = "In the hole in the ground there lived a hobbit"

print(s[:s.index('h')] + s[len(s)-(s[::-1].index('h')):len(s)])