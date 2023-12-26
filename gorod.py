from turtle import *
from random import *

def zemlya(col):
    color(col)
    penup()
    goto(-250,-150)
    pendown()
    begin_fill()
    forward(500)
    right(90)
    forward(100)
    right(90)
    forward(500)
    right(90)
    forward(100)
    end_fill()

def nebo(col):
    color(col)
    penup()
    goto(-250,-150)
    pendown()
    begin_fill()
    for i in range(4):
        forward(500)
        right(90)  
    end_fill()

def sun(x,y,col,size):
    penup()
    goto(x,y)
    pendown()
    color(col)
    begin_fill()
    for i in range(18):
        forward(size)
        left(100)
    end_fill()

zapros = input('Введите время суток')

if zapros == 'день':
    zemlya('lightgreen')
    nebo('lightblue')
    sun(200,200,'yellow',100)

if zapros == 'ночь':
    zemlya('darkgreen')
    nebo('darkblue')
    for i in range(5):
        x = randint(-200,200)
        y = randint(200,350)
        sun(x,y,'white',20)



hideturtle()
exitonclick()
