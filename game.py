from time import sleep

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
        print(self.name,'наносит удар',enemy.name)
        print(enemy.name,'качнулся и потерял',self.power,'здоровья')
        print('Теперь уровень его жизней состовляет', enemy.health - self.power,'хп \n')
        enemy.health = enemy.health - self.power

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

hero = Hero('Леонид',100,20,'меч')
dragon = Hero('Горыныч',200,50,'огонь')
hero.fight(dragon)
