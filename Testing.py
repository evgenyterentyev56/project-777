
# Calculator_v1.1.1 (26.04.2020)_(16:06)

from colorama import Fore, Back, Style
# Передний план: ЧЕРНЫЙ, КРАСНЫЙ, ЗЕЛЕНЫЙ, ЖЕЛТЫЙ, СИНИЙ, МАГЕНТА, ЦИАНОВЫЙ, БЕЛЫЙ, СБРОС.
# Назад: ЧЕРНЫЙ, КРАСНЫЙ, ЗЕЛЕНЫЙ, ЖЕЛТЫЙ, СИНИЙ, МАГЕНТА, ЦИАНОВЫЙ, БЕЛЫЙ, СБРОС.
# Стиль: DIM, NORMAL, BRIGHT, RESET_ALL

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

print(Fore.GREEN)
# what - переменная. input - функция.
what = input(" Что делаем? (+,-,*,/,**,%)")

# float потому что переменная a и b строка, поскольку input - переводит данные к типу данных строка.
# Поэтому строку - мы возвращаем к числу, а именно дробному (float)
# Изначально тип данных строка. При складывании мы получаем 10+10 = 1010.
print(Fore.YELLOW)
a = float(input(" Введи первое число: "))

print(Fore.CYAN)
b = float(input(" Введи второе число: "))


# Условие - что именно делать в зависимости от чего-то. if - Если.
# Условие будет выполненно если в переменной what будет "+"
# Тайпкастинг строки и числа не возможен. Поэтому мы используем str,
# для перевода результата "с" в строку для соединения, знаком +.
# Операция сложения чисел.
if what == "+":
    c = a + b
    print(Fore.MAGENTA)
    print(" Результат: " + str(c))

# Условие - что именно делать в зависимости от чего-то. ilif - Если не выполняется предыдущее условие.
# Условие будет выполненно если в переменной what будет "+"
# Операция вычитания.
elif what == "-":
    c = a - b
    print(Fore.MAGENTA)
    print(" Результат: " + str(c))

# Операция умножения.
elif what == "*":
    c = a * b
    print(Fore.MAGENTA)
    print(" Результат: " + str(c))

# Операция деления.
elif what == "/":
    c = a / b
    print(Fore.MAGENTA)
    print(" Результат: " + str(c))

# Операция возведение в степень.
elif what == "**":
    c = a ** b
    print(Fore.MAGENTA)
    print(" Результат: " + str(c))

# Операция деления по модулю.
elif what == "%":
    c = a % b
    print(Fore.MAGENTA)
    print(" Результат: " + str(c))

# Если не выполняется ни одно из условий.
else:
    print(Fore.RED)
    print(" \"Соси баклажан!\" - Выбрана неверная операция ")


