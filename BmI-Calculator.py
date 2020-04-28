from colorama import Fore, Back, Style
# Передний план: ЧЕРНЫЙ, КРАСНЫЙ, ЗЕЛЕНЫЙ, ЖЕЛТЫЙ, СИНИЙ, МАГЕНТА, ЦИАНОВЫЙ, БЕЛЫЙ, СБРОС.
# Назад: ЧЕРНЫЙ, КРАСНЫЙ, ЗЕЛЕНЫЙ, ЖЕЛТЫЙ, СИНИЙ, МАГЕНТА, ЦИАНОВЫЙ, БЕЛЫЙ, СБРОС.
# Стиль: DIM, NORMAL, BRIGHT, RESET_ALL

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
print(Style.BRIGHT)



what = input('Введите ваши данные, после нажатия на "Enter" ')

a = input("Введите ваш рост (См.)")
b = input("Введите ваш вес (кг.)")
c = input("Введите ваш пол (м/ж)")

if what == "+":
    c = a + b
    print(" Результат " + str(c))

if what == "-":
    c = a - b
    print(" Результат " + str(c))

if what == "*":
    c = a * b
    print(" Результат " + str(c))

if what == "/":
    c = a / b
    print(" Результат " + str(c))
else:
    print(Fore.YELLOW)
    print(Back.CYAN)
    print("WARNING!!!!")