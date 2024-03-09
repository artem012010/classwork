with open('quotes.txt', 'r', encoding='UTF-8') as file:
    data = file.read()
    print(data)

author = input('Введите автора цитаты:')
with open('quotes.txt','a',encoding='UTF-8') as file:
    file.write('\nАвтор:' + author + '\n')

otvet = input('Хотите добавить еще одну цитату?')
while otvet != 'нет':
    with open('quotes.txt','a',encoding='UTF-8') as file:
        quot = input('Введите цитату:')
        author = input('Введите автора:')
        file.write(quot + '\nАвтор:' + author + '\n')
    otvet = input('Хотите добавить еще одну цитату?')

with open('quotes.txt', 'r', encoding='UTF-8') as file:
    data = file.read()
    print(data)



from time import time

summa_ocenok = 0
kolvo_uchenikov = 0
otlichniki = list()

start = time()

with open('pupils.txt', 'r', encoding='UTF-8') as file:
    for pupil in file:
        pupil = pupil.split()
        summa_ocenok += int(pupil[2])
        kolvo_uchenikov += 1
        if pupil[2] == '5':
            otlichniki.append(pupil[0])

end = time()

print('Средний балл:', summa_ocenok/kolvo_uchenikov)
print('Количество отличников',len(otlichniki))
print('Анализ занял:',int(end-start),'с')
        
