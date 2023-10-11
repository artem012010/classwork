print('''
1.Шутка
2.Рекомендация аниме
3.Покупка одежды
4.Игра''')

zapros = input('Введите ваш запрос')
while zapros != 'off':
    if zapros == '1':
        print('Колобок повесился')
    elif zapros == '2':
        genre = input('Введите жанр')
        if genre == 'Сёнен':
            print('Наруто')
        elif genre == 'Романтика':
            print('Твоя апрельская ложь')
        else:
            print('Извините у нас нет такого жанра')
    elif zapros == '3':
        summa = int(input('Сколько у вас денег?'))
        tovar = input('''
        1. Футболка - 100$
        2. Кепка - 30$
        3. Кроссовки - 50$ ''')
        if tovar == '1':
            print('Вы купили футболку', summa - 100,'$')
        if tovar == '2':
            print('Вы купили кепка', summa - 30,'$')
        if tovar == '3':
            print('Вы купили кроссовки', summa - 50,'$')
    elif zapros == '4':
        for i in range(3):
            num = input('Введите число')
            if num == '666':
                print('Вы победили')
                break
            else:
                print('попробуй еще раз')
    else:
        print('Произошла ошибка системы')
    zapros = input('Введите ваш запрос')
    
        print('Извини я не могу распознать твой запрос')
    zapros = input('Введите цифру от 1 до 4')
