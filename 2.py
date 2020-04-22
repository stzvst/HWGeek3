print ("Задание 2")



def everything(n, s_n, b_d, c, em, tel):
    return ["Вы", n, s_n, "рождены",b_d, ", живете в населенном пункте ", c,'. Ваш email', em, ",телефон", tel]


name = input('Введите ваше имя ')
surmane = input("Введите вашу фамилию ")
bd = input("Ваша дата рождения ")
city = input ("В каком городе вы живете? ")
email = input("Ваш email ")
tel = input("Ваш номер телефона ")

otvet = everything(name, surmane, bd, city, email, tel)

for i in otvet:
    print (i,end = ' ')