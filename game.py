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
            if enemy.health <= 0:
                print(enemy.name,'Пал в этом сложном бою')
                break
            sleep(2)
            enemy.attack(self)
            if self.health <= 0:
                print(self.name,'Пал в этом сложном бою')
                break
            sleep(2)

hero = Hero('Леонид',100,30,'Меч')
rogue = Hero('Адольф',100,30,'Усы')
dragon = Hero('Горыныч',150,50,'Огонь')

print('Квест рыцарь и дракон \n')
sleep(2)
print(hero.name,'идет к логову дракона \n')
sleep(2)
print(hero.name,'наткнулся на 3 рейх \n')
sleep(2)
choice = input('Хотите сразиться с Гитлером?')
if choice == 'да':
    hero.fight(rogue)
sleep(2)
if hero.health > 0:
    if hero.health < 100:
        hero.health = 100
        hero.power *= 2
        print(hero.name,'вылечился и стал сильнее')
        print('Теперь уровень его атаки составляет',hero.power)
    sleep(2)
    print('Мы добрались до логова дракона \n')
    print('Да начнется битва \n')
    sleep(2)
    hero.fight(dragon)
    if hero.health > 0:
        print('Получите свое сокровище')
    else:
        print('Конец :(')
    
