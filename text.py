otvet = input('Хотите добавить цитату?')
while otvet != 'нет':
    quot = input('Введите цитату: ')
    author = input('Введите автора: ')
    with open('quotes.txt', 'a', encoding='UTF-8') as file:
        file.write('\n' + quot + '\nАвтор: ' + author )
    otvet = input('Хотите добавить цитату?')

with open('quotes.txt', 'r', encoding='UTF-8') as file:
    data = file.read()
    print(data)


from time import time
summa = 0
kolvo = 0
otlichniki = list()

start = time()

with open('pupils.txt', 'r', encoding='UTF-8') as file:
    for pupil in file:
        pupil = pupil.split()
        summa += int(pupil[2])
        kolvo += 1
        if pupil[2] == '5':
            otlichniki.append(pupil[0])

end = time() 

print('Средний балл учеников', summa/kolvo)
print('Количество отличников:', len(otlichniki))
print(end - start, 'с')
