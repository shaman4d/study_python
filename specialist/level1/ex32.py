# Даны два целых числа - координаты клетки на шахматной доске. Первое число от 1 до 8 обозначает
# вертикаль снизу вверх, второе - горизонталь слева направо.
# Шахматная доска
# Напечатайте слово "Белая", если клетка на данных координатах белая и "Чёрная", если клетка чёрная.

col = 1
row = 2

print("White" if (col  + (1 if row % 2 == 0 else 0))  % 2 == 0 else "Black")