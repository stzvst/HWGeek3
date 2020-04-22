print("Задание 3")



def my_func(a,b,c):
    all = [a, b, c]
    max_all_1 = int(max(all))
    all.remove(max_all_1)
    max_all_2 = max(all)
    print ("Наибольшие два числа - это", max_all_1, 'и', max_all_2)
    return  max_all_1 + max_all_2

first = int(input("Введите первое число "))
second = int(input("Введите второе число "))
third = int(input("Введите третье число "))

otv = my_func(first,second,third)
print ('Их сумма' ,otv)