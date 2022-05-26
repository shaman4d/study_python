# На вход подаётся строка, в которой несколько раз встречается вхождение буквы "h".
# Напечатайте эту строку заменив все буквы "h" на "H". кроме её первого и последнего вхождения.
# Пример ввода
# In the hole in the ground there lived a hobbit
# Пример вывода
# In the Hole in tHe ground tHere lived a hobbit

s = "In the hole in the ground there lived a hobbit"

print("".join( [i if i != 'h' else 'H' for i in s ] ))