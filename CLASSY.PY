from random import *

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


hero = Hero('Артур',100,10,'меч')
dragon = Hero('Смауг',200,30,'пламя')
hero.strike(dragon)
dragon.strike(hero)
