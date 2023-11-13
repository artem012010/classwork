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

background(-250,-100,500,100,'lightgreen')
background(-250,500,500,600,'lightblue')
exitonclick()
