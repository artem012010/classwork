otdel = {
    'Пушкин': { 'портфолио': ['WoT','GTA5','Genshin'],
    'должность': 'Ген директор', 'эффективность': 100}, 
    'Гитлер': {'портфолио': ['Doom','Among us','Genshin'],
    'должность': 'Бизнес аналитик', 'эффективность': 99},
    'Ленин': {'портфолио': ['Комунизм','Among us','Genshin'],
    'должность': 'Сторож', 'эффективность': 200},
}

zapros = input('1 - фамилии всех сотрудников 2 - самый эффективный 3 - Должности')
while zapros != 'off':
    if zapros == '1':
        for surname in list(otdel.keys()):
            print(surname)
    if zapros == '2':
        kolvo_sotrudnikov = len(otdel)
        surnames = list(otdel.keys())
        effectivnost = []
        for i in range(kolvo_sotrudnikov):
            effectivnost.append(otdel[surnames[i]]['эффективность'])
        effectivnost.sort()
        print('Максимальная эффективность',effectivnost[-1])
    if zapros == '3':
        surnames = list(otdel.keys())
        for surname in surnames:
            print(otdel[surname]['должность'])

    zapros = input('1 - фамилии всех сотрудников 2 - самый эффективный 3 - Должности')

