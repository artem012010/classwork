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

hero = Hero('Артур',100,10,'меч')
hero.info()
