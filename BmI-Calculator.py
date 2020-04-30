from colorama import Fore, Back, Style
# Передний план: ЧЕРНЫЙ, КРАСНЫЙ, ЗЕЛЕНЫЙ, ЖЕЛТЫЙ, СИНИЙ, МАГЕНТА, ЦИАНОВЫЙ, БЕЛЫЙ, СБРОС.
# Назад: ЧЕРНЫЙ, КРАСНЫЙ, ЗЕЛЕНЫЙ, ЖЕЛТЫЙ, СИНИЙ, МАГЕНТА, ЦИАНОВЫЙ, БЕЛЫЙ, СБРОС.
# Стиль: DIM, NORMAL, BRIGHT, RESET_ALL
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
print(Style.NORMAL)
print(Fore.GREEN)

print('Введите ваши данные:')
print(Fore.BLUE)
# Получаем данные от пользователя

b = float(input("Введите ваш рост (м./Пример. 1,72)"))
c = int(input("Введите ваш вес (кг.)"))



# Вычисления
bmi = c / b ** 2
bmi = str(round(bm))
print("Результат " + bm)

if bmi == "22":
    print("Резульат ")