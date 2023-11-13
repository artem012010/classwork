from turtle import *

def ground():
    color('lightgreen')
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

def sky():
    color('lightblue')
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
