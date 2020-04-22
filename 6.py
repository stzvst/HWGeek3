print ('Задание 6')


def int_func(word):
    word = word.upper()[:1] + word [1:]
    return word



text = input('Введите слово или текс через пробел ')
text = text.split()
i = 0
big_text = ('')
while i <= len(text)-1:
    lil_text = text[i]
    lil_text = int_func(lil_text)
    print(lil_text)
    text[i] = lil_text
    print(text)
    big_text = big_text + (' ') +  text[i]
    i = i+1



print ("Вывод", big_text)







