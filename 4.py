print ("Задача 4")



def my_func(x,y):
    if x < 0 or y >= 0:
        print ("Значения введины неверно")
        return ("Все плохо")
    else:
        y = int(-y)
        otv = x
        for i in range(y-1):

            otv = otv*x
        otv = 1/otv
        return otv

a = float(input("Введите положительное число "))
b = float(input("Введите отрицательное число "))
z = my_func(a,b)
print ('Число', a, "в степени", b, "будет равяться", z)
