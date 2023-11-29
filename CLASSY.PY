from random import *
from time import *

class Hero():
    def __init__(self,name,hp,power,weapon):
        self.name = name
        self.hp = hp
        self.power = power
        self.weapon = weapon
    
        

    def info(self):
        print('Имя персонажа:',self.name)
        print('Ур хп',self.hp,'Ур атк',self.power)
        print('Оружие персонажа',self.weapon)

    def strike(self,enemy):
        print(self.name,'наносит удар',enemy.name,'с помощью',self.weapon)
        print('уровень здоровья',enemy.name,'понизился c', enemy.hp)
        enemy.hp = enemy.hp - randint(self.power-5,self.power+5)
        print('Теперь он составляет',enemy.hp,'\n')

    def fight(self,enemy):
        while True:
            self.strike(enemy)
            sleep(2)
            enemy.strike(self)
            sleep(2)
            if enemy.hp < 0 and self.hp < 0 :
                print('В бою пали оба')
                break
            if enemy.hp < 0:
                print(enemy.name,'Проиграл сражение')
                break
            if self.hp < 0:
                print(self.name,'Потерпел порожение')
                break
