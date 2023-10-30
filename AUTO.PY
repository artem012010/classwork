#Код первого файла - название любое

from sport_analyser import analyser

zapros = input('Что бы вы хотели узнать?')
while zapros != 'off':
    analyser( zapros )
    zapros = input('Что бы вы хотели узнать?')




#Код второго файла назвать желательно sport_analyser

def analyser(zapros):

    result = zapros.find('тренер')
    if result != -1:
        trainer_info()

    result = zapros.find('оплата')
    if result != -1:
        oplata()

def trainer_info():
    print('Александр Невский 10 лет опыта Любит стероиды')

def oplata():
    trenirovki = int(input('Сколько тренировок вы посетели'))
    print('Ваша оплата состовляет', trenirovki * 800, 'с')
