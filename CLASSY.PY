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
        print('Оружие персонажа:',self.weapon)
        print('Здоровье:',self.hp,'Атака:',self.power)

    def strike(self,enemy):
        print(self.name,'нанес удар',enemy.name)
        enemy.hp = enemy.hp - randint(self.power-5,self.power+5)
        print(enemy.name,'ранен')
        print('Теперь его уровень жизни составляет:',enemy.hp,'\n')


    def fight(self,enemy):
        while True:
            self.strike(enemy)
            sleep(1)
            if enemy.hp < 0:
                print(enemy.name,'проиграл бой')
                break
            enemy.strike(self)
            sleep(1)
            if self.hp < 0:
                print(self.name,'проиграл бой')
                break

hero = Hero('Артур',100,30,'меч')
goblin = Hero('Вася',60,15,'камень')
hero.fight(goblin)
