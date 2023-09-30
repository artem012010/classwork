test_results = [
   [85.4, 71.6, 93.2, 65.8, 45.0],
   [89.5, 80.0, 95.5, 76.5, 72.0]
]

average = 0
for result in test_results[0]:
   average += result
print('Средний результат «до»:', average/len(test_results[0]))

average = 0
for result in test_results[1]:
   average += result
print('Средний результат «после»:', average/len(test_results[1]))


departments = {
   'продажи':{
       'сотрудники': ['Гришин', 'Иванова'],
       'менеджер': 'Иванова',
       'заведующий': 'Гришин'
   },
   'разработка':{
       'сотрудники': ['Васильев', 'Ежов', 'Петрова'],
       'менеджер': 'Ежова',
       'заведующий': 'Петрова'
   }
}
print('Заведующие отделов:')
for department in departments:
   print('-', departments[department]['заведующий'])
  
print('Проектные менеджеры отделов:')
for department in departments:
   print('-', departments[department]['менеджер'])




trainings = {
   'Онбординг':{
       'ответственный': 'Ершов В.С.',
       'темы': ['техника безопасности', 'работа в команде'],
       'дата': '15.05'
   },
   'Повышение квалификации':{
       'ответственный': 'Мишин Н.В.',
       'темы': ['лидерство', 'компьютерная грамотность'],
       'дата': '20.11'
   }
}
print('Тренинги ProTeam')
print('1-названия тренингов, 2-инфо о тренинге')
action = input('Номер действия (off-выйти):')
while action != 'off':
   if action == '1':
       for training in trainings:
           print('-', training)
   if action == '2':
       title = input('Название тренинга:')
       if title in trainings:
           print(trainings[title]['ответственный'])
           print(trainings[title]['темы'])
           print(trainings[title]['дата'])
       else:
           print('Такого тренинга не существует!')
   action = input('Номер действия (off-выйти):')



sotrudniki = {
    'Путин': {
        'Дожность': 'БОСС',
        'Эффективность': 90,
        'Проекты': ['первый', 'второй', 'третий']
    },
    'Байден': {
        'Дожность': 'БОСС',
        'Эффективность': 100,
        'Проекты': ['первый', 'второй', 'третий']
    },
    'Си': {
        'Дожность': 'БОСС',
        'Эффективность': 101,
        'Проекты': ['первый', 'второй', 'третий']
    },
}

print('1\Фамилия всех сотрудников, 2\Самый эффективный 3\Проекты')
result = int(input('Введите число:'))
while result != 'off':
    if result == 1:
        for surname in sotrudniki:
            print(surname)
    elif result == 2:
        kef = 0
        for surname in sotrudniki:
            kef += sotrudniki[surname]['Эффективность']
        print('Коэфицент эффективности:', kef/len(sotrudniki))
    elif result == 3:
        name = input('Какой сотрудник вас интересует?')
        if name in sotrudniki:
            print('Проекты:',sotrudniki[name]['Проекты'])
        else:
            print('Такого у нас нету')
    result = input('Введите число:')
