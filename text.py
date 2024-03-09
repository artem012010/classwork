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
