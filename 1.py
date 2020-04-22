print ('Задание 1')




def delen(x,y):
    if y == 0:
        print ("На ноль человечество делить еще не научилось")
        return ('Ничего')
    else:
      return x / y



a = int(input("Введите знаменатель "))
b = int(input("Введите делитель "))

z = delen(a,b)
print (a, "деленное на", b, "равняется", z)