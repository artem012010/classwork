otdel_dizaina = {
    'Пушкин': {
        'портфолио': ['WoT','GTA5'],
        'профиль': 'Анимешник',
    }
}
surname = input('Введите фамилию')
if surname in otdel_dizaina:
    print('Фамилия',surname)
    print('Первая работа автора',otdel_dizaina[surname]['портфолио'][0])
    print('Должность:',otdel_dizaina[surname]['профиль'])
else:
    otdel_dizaina[surname] = dict()
    portfolio = input('Введите проекты').split()
    otdel_dizaina[surname]['портфолио'] = portfolio
    otdel_dizaina[surname]['профиль'] = input('Введите должность')


    

