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

# Запрос данных у пользователя
b = input("Введите ваш рост (Ед.изм.(М.)/Пример. 1,72)")
c = input("Введите ваш вес (Ед.изм.(кг.))")
b = float(b)


# Вычисление bmi
print(Fore.RED)
b = b * 2
bmi = float(c) / b
bmi = round(bmi)



if bmi < 20:
    print("Недостаточная масса тела" )

elif bmi == 20:
    print("Норма")
elif bmi == 21:
    print("Норма")
elif bmi == 22:
    print("Норма")
elif bmi == 23:
    print("Норма")
elif bmi == 24:
    print("Норма")
elif bmi == 25:
    print("Норма")


else:
    print("Пиздец ты, жирный!!!!")






