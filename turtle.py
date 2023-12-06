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

# Создаем персонажей
player = Sprite(0,-100,10,'circle','black')
gold = Sprite(0,80,0,'triangle','gold')

screen = player.getscreen() # Создаем обьект экрана
screen.listen() # Просим экран слушать клавиши
#Подписки на события клавиатуры
screen.onkey(player.move_up,'Up') 
screen.onkey(player.move_down,'Down') 
screen.onkey(player.move_right,'Right') 
screen.onkey(player.move_left,'Left') 

