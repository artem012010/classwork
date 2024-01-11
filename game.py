from turtle import *
from time import *
from random import *

adolf = Turtle()
adolf.color('blue')
adolf.shape('turtle')
adolf.penup()
adolf.points = 0

def poimali(x,y):
    adolf.write('ВАЙ?',font=('Arial',20,'normal'))
    adolf.points += 1
    adolf.goto(randint(-200,200),randint(-200,200))

adolf.onclick(poimali)

while adolf.points < 3:
    adolf.goto(randint(-200,200),randint(-200,200))
    sleep(1)

adolf.clear()
adolf.goto(-100,-50)
adolf.write('Ты победил',font=('Arial',30,'bold'))
adolf.hideturtle()


