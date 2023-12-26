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


def dom():
    color('gray')
    penup()
    goto(-100,-150)
    pendown()
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()
    forward(100)
    color('red')
    left(90)
    begin_fill()
    for i in range(3):
        forward(100)
        right(120)
    end_fill()


zemlya('lightgreen')
nebo('lightblue')
dom()



hideturtle()
exitonclick()
