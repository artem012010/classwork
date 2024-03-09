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

