# Код основной программы не важно как называется допустим zeus.py
from time import *
from analizator import *

print('Вас приветствует спортивный центр ЗЕВС')
start = time() 
zapros = input('Что бы вы хотели узнать?')
while zapros != 'выйти':
    otvet(zapros)
    zapros = input('Еще что нибудь (выйти - завершение)?')

end = time() 
print('Было приятно пообщаться вы пробыли с нами')
print(int((end - start)/60),'минут')

#Код модуля важно назвать как импорт из основной программы в моем случае analizator.py
from random import randint

def otvet(zapros):
    zapros = zapros

    if zapros.find('трени') != -1:
        raspisanie()

    if zapros.find('оплат') != -1 or zapros.find('деньг') != -1:
        oplata()

    if zapros.find('игра') != -1:
        ugaday()

def raspisanie():
    print('Плавание вт\чт 20:00')
    print('Футбол сб\вс 16:00')

def oplata():
    trenirovka = int(input('Сколько занятий вы посетили'))
    print('Вы должны оплатить',trenirovka * 500,'сом')

def ugaday():
    win = randint(1,10)
    for i in range(3):
        num = int(input('Введите число'))
        if num == win:
            print('Вы победили')
            break
        else:
            print('попробуй еще раз')
