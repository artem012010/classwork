from time import sleep
from random import randint

class Hero():
    def __init__(self,name,health,power,weapon):
        self.name = name
        self.health = health
        self.power = power
        self.weapon = weapon

    def story(self):
        print('Меня зовут', self.name)
        print('Уровень моего здоровья', self.health)
        print('Я сражаюсь', self.weapon,'и наношу',self.power,'урона')

    def attack(self,enemy):
        enemy.health = enemy.health - self.power * (randint(10,20)*0.1)
        print(self.name,'наносит удар',enemy.name)
        print('Теперь уровень его жизней состовляет', enemy.health,'хп \n')


    def fight(self,enemy):
        while self.health > 0 and enemy.health > 0:
            self.attack(enemy)
            sleep(2)
            enemy.attack(self)
            sleep(2)
        if enemy.health <= 0:
            print(enemy.name,'Пал в этом сложном бою')
        else:
            print(self.name,'Пал в этом сложном бою')

hero = Hero('Леонид',100,30,'меч')
dragon = Hero('Горыныч',150,50,'огонь')
hero.fight(dragon)
