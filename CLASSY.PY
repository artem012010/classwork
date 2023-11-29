#Создайте модуль и запомните его имя например game

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


#файл второй с сюжетом нашего квеста

from game import *

print('Доблестный рыцарь отправился в путешествие за сокровищами \n')
sleep(1)
hero = Hero('Артур',100,30,'меч')
hero.info()
print('Наш рыцарь натыкается на логово гоблин \n')
sleep(1)
otvet = input('Хотите сразиться? \n')
if otvet == 'да':
    goblin = Hero('Эдик',80,20,'лук')
    goblin.info()
    print('\n')
    sleep(1)
    hero.fight(goblin)
    if goblin.hp < 0:
        hero.hp = 100
        hero.power *= 2
        print('Наш рыцарь стал сильнее')
        print('Теперь уровень его здоровья и атаки равен')
        print(hero.hp,'/',hero.power)


print('Мы наконец то достигли пещеры дракона \n')
sleep(1)
print('Да начнется битва \n')
sleep(1)
dragon = Hero('Смауг',150,40,'пламя')
dragon.info()
print('\n')
hero.fight(dragon)
if dragon.hp < 0:
    print('Вы забрали сокровище ПОЗДРОВЛЯЕМ!!!!')
else:
    print('Вы погибли как настоящий рыцарь')

