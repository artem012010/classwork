#Первый файл является модулем допустим с названием city
from turtle import *

def background(x,y,wid,hei,col):
    color(col)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    forward(wid)
    right(90)
    forward(hei)
    right(90)
    forward(wid)
    right(90)
    forward(hei)
    right(90)
    end_fill()

def sun():
    penup()
    goto(170,100)
    pendown()
    color('yellow')
    begin_fill()
    for i in range(18):
        forward(75)
        left(100)
    end_fill()


def moon():
    penup()
    goto(200,100)
    pendown()
    color('white')
    begin_fill()
    circle(50)
    end_fill()

#Второй файл основная часть программы название любое допустим main
from turtle import *
from city import *

speed(10)

time = input('Введите время суток')
if time == 'день':
    background(-250,-100,500,100,'lightgreen')
    background(-250,400,500,500,'lightblue')
    sun()
if time == 'ночь':
    background(-250,-100,500,100,'darkgreen')
    background(-250,400,500,500,'darkblue')
    moon()


hideturtle()
exitonclick()
