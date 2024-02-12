Ответы на задания

Задание 1. «Тренинг»
1.2. Программа после исправления ошибок:
question = input('Введите ваш вопрос(off - закрыть чат)')
while question != 'off':
    if question != '':
        print('Обращение отправлено.')  
    question = input('Введите ваш вопрос(off - закрыть чат)') 
print('До свидания!')

1.3. Программа :
question = input('Задай вопрос (стоп - завершить):')
while question != 'стоп':
    if question == 'Как тебя зовут?':
        print('Меня зовут Кристина.')
    elif question == 'У тебя есть хобби?':
        print('Я люблю рисовать.')
    elif question == '':
        print('Спросите меня что-нибудь.')
    else:
        print('К сожалению, я тебя не понимаю.')
    question = input('Задай вопрос (стоп - завершить):')  



1.4. Завершённая программа:
true_month = '7'
true_year = '2007'


for i in range(5):
    month = input('Месяц:')
    year = input('Год:')
    if month == true_month: 
        if year == true_year:
            print('Вы выиграли!')
            break
        else:
            print('Вы угадали месяц!')
    else:
        if year == true_year:
            print('Вы угадали год!')
        else:
            print('Неверные месяц и год.')



Доп задание 1.1.
#магазин коинов
coins = 100
print('Ваши коины:', coins)
choice = input('1 - магазин, 2 - посмотреть рекламу(+5), 3 - выйти')
while choice != '3':
    if choice == '1':
        choice_market = input('1 - стикер (50), 2 - футболка(100)')
        if choice_market == '1':
            coins -= 50
        elif choice_market == '2':
            coins -= 100
    elif choice == '2':
        coins +=5
    print('Ваши коины:', coins)
    choice = input('1 - магазин, 2 - посмотреть рекламу(+5), 3 - выйти')



Доп задание 1.3




Задание 2. «Хакатон»
	Творческое задание, аналогичное предыдущим разобранным задачам. Выполняется в Лаборатории без автопроверки.


Дополнительное задание «Тренинг: доп. задания»
1.1. Программа после исправления ошибок:
amount = int(input('Количество:'))
for i in range(amount):
    age = int(input('Возраст:'))
    if age < 14:
        print('Недостаточный возраст')


1.2. Программа:
ingredient = input('главный ингредиент(стоп - завершить):')
while ingredient != 'стоп':
    time = input('1 - 30 минут, 2 - 1 час')
    if ingredient == 'творог':
        if time == '1':
            print('Запеканка')
        elif time == '2':
            print('Сырники')
    elif ingredient == 'курица':
        if time == '1':
            print('Куриное филе в сметане')
        elif time == '2':
            print('Спагетти с курицей в сливочно-грибном соусе')
    else:
        if time == '1':
            print('Салат с брокколи')
        elif time == '2':
            print('Суп-пюре из шампиньонов')
    ingredient = input('главный ингредиент(стоп - завершить):')






sotrudniki = {
    'Айзек Кларк':
    {
        'должность': 'главный разработчик',
        'эффективность': 90,
        'проекты': ['Dead Space','Calisto Protocol']
    },
    'Серьезный Сэм':
    {
        'должность': 'геймдизайнер',
        'эффективность': 66,
        'проекты': ['Serios Sam','Worms']
    },
    'DoomGuy':
    {
        'должность': 'тестировщик',
        'эффективность': 99,
        'проекты': ['Doom','Sims 3']
    },
}

print('Добро пожаловать в Steam Company')
otvet = input('1 - имена \n2 - самый эффективный сотрудник \n3 - должность сотрудника')
while otvet != 'стоп':
    if otvet == '1':
        print('Имена всех сотрудников:')
        for name in sotrudniki:
            print(name)
    otvet = input('1 - имена \n2 - самый эффективный сотрудник \n3 - должность сотрудника')













