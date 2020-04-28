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