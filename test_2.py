
what=input("Выберите мат. действие: ")
elif what == "!":
 fac()

def fac():
 n = int (input ())
 f = 1
 for i in range (1, n + 1):
     f = f * i
 print ('Результат вычисления факториала числа: '+str(f))