print('Привет я бот Олег')
print('Я умею всякое')
zapros = input('Что вас интересует?')
while zapros.find('вык') == -1:
    if zapros == 'шутка':
        print('Русалка села на шпагат')
    elif zapros == 'аниме':
        genre = input('Введите жанр')
        if genre == 'боевик':
            print('Токийские мстители')
        elif genre == 'романтика':
            print('Сад изящных слов')
        else:
            print('не знаком с таким')
    elif zapros == 'игра':
        for i in range(3):
            num = int(input('Введи число'))
            if num == 7:
                print('Вы победили')
                break
            else:
                print('Попробуй еще раз')
    elif zapros == 'купить' or zapros == 'шмот':
        print('В нашем магазине есть')
        print('Куртка - 7000 Шапка - 1000')
        money = int(input('Сколько у вас денег'))
        dress = input('Что вас заинтересовало')
        if dress == 'куртка' and money >= 7000:
            print('Вы купили куртку')
            print('У вас осталось',money - 7000,'$')
        elif dress == 'шапка' and money >= 1000:
            print('Вы купили шапку')
            print('У вас осталось',money - 1000,'$')
        else:
            print('У нас такого нет')
    else:
        print('Извини я тебя не понимаю')
        print('Напиши шутка - аниме - игра - купить')
    zapros = input('Что вас интересует?')
print('Приятно было пообщаться')

