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

clock = Turtle()
clock.penup()
clock.goto(-150,100)

def timer():
    past = int(time() - start)
    clock.hideturtle()
    clock.clear()
    clock.write(str(past), font=('Arial',30,'bold'))
    return past
  
def rand_move():
    oleg.goto(randint(-200,200),randint(-200,200))

def poimali(x,y):
    oleg.write('Вааай',font=('Arial',20,'normal'))
    rand_move()
    oleg.point += 1

def result(text,col):
    oleg.color(col)
    oleg.clear()
    oleg.goto(-100,0)
    oleg.write(text, font=('Arial',50,'bold'))
    oleg.hideturtle()

oleg.onclick(poimali)

start = time()
while oleg.point < 3 and timer() < 10:
    timer()
    rand_move()
    sleep(0.5)

if oleg.point == 3:
    result('ПОБЕДА','green')
else:
    result('ПРОИГРЫШ','red')
