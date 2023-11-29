class Hero():
    def __init__(self,name,hp,power,weapon):
        self.name = name
        self.hp = hp
        self.armor = 100
        self.power = power
        self.weapon = weapon
        self.info()

    def info(self):
        print('Имя персонажа:',self.name)
        print('Оружие персонажа:',self.weapon)
        print('Здоровье:',self.hp,'Атака:',self.power)

hero = Hero('Артур',100,10,'меч')


