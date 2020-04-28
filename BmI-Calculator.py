from colorama import Fore, Back, Style
# Передний план: ЧЕРНЫЙ, КРАСНЫЙ, ЗЕЛЕНЫЙ, ЖЕЛТЫЙ, СИНИЙ, МАГЕНТА, ЦИАНОВЫЙ, БЕЛЫЙ, СБРОС.
# Назад: ЧЕРНЫЙ, КРАСНЫЙ, ЗЕЛЕНЫЙ, ЖЕЛТЫЙ, СИНИЙ, МАГЕНТА, ЦИАНОВЫЙ, БЕЛЫЙ, СБРОС.
# Стиль: DIM, NORMAL, BRIGHT, RESET_ALL

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
print(Style.BRIGHT)



print('Введите ваши данные и нажмите клавишу "Enter":')

# Получаем данные от пользователя
a = float(input("Введите ваш рост (См.)"))
b = float(input("Введите ваш вес (кг.)"))

# Вычисления
c = a * 2
d = b / c * 100
print("Результат " + str(d))

if d >= "20":
    print("Ok")




