# Дано целое положительное число из трёх отличных друг от друга цифр.
# Напечатайте "Да", если цифры следуют друг относительно друга в восходящем порядке слева
# направо и "Нет", если это не так.
n = 193
a,b,c = map(int,list(str(n)))
print("Yes" if a < b and b < c else "No")
