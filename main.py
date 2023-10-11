print('''1 - расскажи шутку 2 - аниме
3 - купить сувениры 4 - сыграть в игру''')
zapros = input('Введите цифру от 1 до 4')
while zapros != 'off':
    if zapros == '1':
        print('Колобок повесился')
    elif zapros == '2':
        anime = input('Какой жанр вы предпочитаете')
        if anime == 'боевик':
            print('Семья Шпиона')
        elif anime == 'сёнен':
            print('Драгон бол/ Хелсинг / Наруто')
        elif anime == 'хоррор':
            print('Рыба/ Дзюнзи Ито')
        elif anime == 'исекай':
            print('Бродяги/ Overlord')
        else:
            print('Такого жанра у нас нет')
    elif zapros == '3':
        summa = int(input('Сколько у вас денег?'))
        choice = input('1 - Фигурка Дэнжи (1000$) 2 - Меч Гатса (500$)')
        if choice == '1':
            print('Вы купили фигурку дэнжи у вас осталось', summa - 1000,'$')
        if choice == '2':
            print('Вы купили меч гатса у вас осталось', summa - 500,'$')
    elif zapros == '4':
        print('Вы зашли в игру угадай число у вас есть 3 попытки')
        win_number = 666
        for i in range(3):
            num = int(input('Введи число'))
            if num == win_number:
                print('Вы победили')
                break
            else:
                print('Попробуй еще раз')
    else:
        print('Извини я не могу распознать твой запрос')
    zapros = input('Введите цифру от 1 до 4')
