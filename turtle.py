# Подключи нужные модули
from turtle import *
from random import *
from time import *
oleg = Turtle()
oleg.penup()
oleg.shape('turtle')
oleg.color('blue')
oleg.speed(10)
oleg.point = 0

def rand_move():
    oleg.goto(randint(-200,200),randint(-200,200))

def poimali(x,y):
    oleg.write('Вааай',font=('Arial',20,'normal'))
    rand_move()
    oleg.point += 1

def win():
    oleg.clear()
    oleg.goto(-100,0)
    oleg.write('ПОБЕДА', font=('Arial',50,'bold'))
    oleg.hideturtle()

oleg.onclick(poimali)
while oleg.point < 3:
    rand_move()
    sleep(2)

win()
