print ('Задание 5')




def super_prog(zumma):
    choise = input('Введите еще числа через пробелы или наберите Q для завершения цикла программы ')
    key = ["Q"]
    choise = choise.split()
    print(choise)
    if choise == key:
        print("Закрываем лавочку")
        return
    elif key[0] in choise:
        choise.remove("Q")
        i = 0
        while i < len(choise):
            choise[i] = int(choise[i])
            i = i + 1
        lil_summa = sum(choise)
        zumma = zumma + lil_summa
        print("Сумма нового списка равна", lil_summa)
        print("В сумме с предыдущим значением будет", zumma)
        return zumma
    else:
        i = 0
        while i < len(choise):
            choise[i] = int(choise[i])
            i = i + 1
        lil_summa = sum(choise)
        zumma = zumma + lil_summa
        print("Сумма нового списка равна", lil_summa)
        print("В сумме с предыдущим значением будет", zumma)
        super_prog(zumma)




def prog():
    chisla = input("Введите числа через пробелы ")
    new_chisla = chisla.split()
    i = 0
    while i < len(new_chisla):
        new_chisla[i] = int(new_chisla[i])
        i = i + 1
    summa = sum(new_chisla)
    print (summa)
    mini_otv = super_prog(summa)
    return mini_otv




otvet = prog()
print(otvet)