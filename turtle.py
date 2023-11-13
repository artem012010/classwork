#Главный файл основная часть программы допустим main.py
from turtle import *
from gorod import *

speed(10)

time = input('Введите время суток')
if time == 'день':
    ground('lightgreen')
    sky('lightblue')
    home()
    sun()
if time == 'ночь':
    ground('darkgreen')
    sky('darkblue')
    home()
    moon()

hideturtle()
exitonclick()

#Второй файл с функциями для отрисовки обьектов допустим city.py
from turtle import *

def ground(col):
    color(col)
    penup()
    goto(-250,-100)
    pendown()
    begin_fill()
    for i in range(2):
        forward(500)
        right(90)
        forward(100)
        right(90)
    end_fill()

def sky(col):
    color(col)
    penup()
    goto(-250,200)
    pendown()
    begin_fill()
    for i in range(2):
        forward(500)
        right(90)
        forward(300)
        right(90)
    end_fill()

def sun():
    color('yellow')
    penup()
    goto(180,130)
    pendown()
    begin_fill()
    for i in range(18):
        forward(70)
        left(100)
    end_fill()


def moon():
    color('white')
    penup()
    goto(180,100)
    pendown()
    begin_fill()
    circle(50)
    end_fill()

def home():
    color('orange')
    penup()
    goto(-180,-100)
    pendown()
    begin_fill()
    for i in range(4):
        forward(50)
        left(90)
    end_fill()

    left(90)
    forward(50)
    right(90)
    color('red')
    begin_fill()
    for i in range(3):
        forward(50)
        left(120)
    end_fill()


