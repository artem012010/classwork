#создай класс Converter
class Converter():
    def __init__(self,rub,usd):
        self.rub = rub
        self.usd =usd

    def convert_usd(self,kurs):
        print('Вы получите',self.usd * kurs,'р')

    def convert_rub(self,kurs):
        print('Вы получите',self.rub / kurs,'$')

rub = int(input('Введите количество рублей'))
usd = int(input('Введите количество долларов'))
kurs = float(input('Введите курс валюты'))
robot = Converter(rub,usd)
otvet = input('Что вы хотите конвертировать руб\дол')
if otvet == 'руб':
    robot.convert_rub(kurs)
if otvet == 'дол':
    robot.convert_usd(kurs)
