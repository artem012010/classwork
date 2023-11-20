from turtle import *
from random import randint
from time import *

oleg = Turtle()
oleg.shape('turtle')
oleg.color('blue')
oleg.speed(10)
oleg.penup()

clock = Turtle()
clock.penup()

oleg.points = 0

def rand_move():
    oleg.goto(randint(-200,200), randint(-200,200))

def touch(x,y):
    oleg.write('Вай',font=('Arial',20,'normal'))
    rand_move()
    oleg.points += 1

def result(text):
    oleg.clear()
    oleg.goto(-100,0)
    oleg.write(text,font=('Arial',50,'bold'))
    oleg.hideturtle()

def timer():
    clock.goto(-200,100)
    t = abs(start - time())
    vremya = str(round(t,1))
    clock.clear()
    clock.hideturtle()
    clock.write(vremya,font=('Arial',30,'bold'))
    return t
    
oleg.onclick(touch)
start = time()
while oleg.points < 3 and timer() < 20:
    rand_move()
    sleep(0.5)
    timer()

if timer() >= 20:
    result('Проигрыш')
else:
    result('Победа')
