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

    #Правила движения
    def move_set(self,start_x,start_y,end_x,end_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.goto(start_x,start_y)
        self.setheading(self.towards(end_x,end_y))

    #Движение врагов
    def make_step(self):
        self.forward(self.step)
        if self.distance(self.end_x,self.end_y) < self.step:
            self.move_set(self.end_x,self.end_y,self.start_x,self.start_y)

# Создаем персонажей
player = Sprite(0,-100,10,'circle','black')
gold = Sprite(0,80,0,'triangle','gold')
enemy1 = Sprite(-50,30,5,'turtle','red')
enemy2 = Sprite(50,-30,5,'turtle','red')
enemy1.move_set(-100,30,100,30)
enemy2.move_set(100,-30,-100,-30)

screen = player.getscreen() # Создаем обьект экрана
screen.listen() # Просим экран слушать клавиши
#Подписки на события клавиатуры
screen.onkey(player.move_up,'Up') 
screen.onkey(player.move_down,'Down') 
screen.onkey(player.move_right,'Right') 
screen.onkey(player.move_left,'Left') 

point = 0

while point < 3:

    enemy1.make_step()
    enemy2.make_step()

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
