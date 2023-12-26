from turtle import *

def zemlya():
    color('lightgreen')
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

def nebo():
    color('lightblue')
    penup()
    goto(-250,-150)
    pendown()
    begin_fill()
    for i in range(4):
        forward(500)
        right(90)  
    end_fill()

zemlya()
nebo()
exitonclick()
