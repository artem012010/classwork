from turtle import *

# Игровой класс для создания спрайтов
class Sprite(Turtle):
    def __init__(self,x,y,step,shape,color):
        super().__init__()
        self.penup()
        self.shape(shape)
        self.color(color)
        self.goto(x,y)
        self.step = step

    #Функции обработчики движений
    def move_up(self):
        self.goto(self.xcor(),self.ycor() + self.step)
    def move_down(self):
        self.goto(self.xcor(),self.ycor() - self.step)
    def move_right(self):
        self.goto(self.xcor() + self.step,self.ycor())
    def move_left(self):
        self.goto(self.xcor() - self.step,self.ycor())

    #Проверка столкновений
    def is_collide(self,sprite):
        dist = self.distance(sprite.xcor(),sprite.ycor())
        if dist < 30:
            return True
        else:
            return False

# Создаем персонажей
player = Sprite(0,-100,10,'circle','black')
gold = Sprite(0,80,0,'triangle','gold')
enemy1 = Sprite(-50,30,0,'turtle','red')
enemy2 = Sprite(50,-30,0,'turtle','red')

screen = player.getscreen() # Создаем обьект экрана
screen.listen() # Просим экран слушать клавиши
#Подписки на события клавиатуры
screen.onkey(player.move_up,'Up') 
screen.onkey(player.move_down,'Down') 
screen.onkey(player.move_right,'Right') 
screen.onkey(player.move_left,'Left') 

point = 0

while point < 3:

    if player.is_collide(gold):
        point += 1
        player.goto(0,-100)

    if player.is_collide(enemy1) or player.is_collide(enemy2):
        gold.hideturtle()
        player.goto(-50,-20)
        player.write('Вы проиграли',font=('Arial',30,'bold'))
        break

if point == 3:
    player.goto(-50,-20)
    player.write('Вы победили',font=('Arial',30,'bold'))
