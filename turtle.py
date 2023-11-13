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
