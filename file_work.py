from turtle import *

def light_on(x,y,col):
    penup()
    goto(x,y)
    pendown()
    color(col)
    begin_fill()
    circle(30)
    end_fill()

def light_off(x,y):
    penup()
    goto(x,y)
    pendown()
    circle(30)

light_on(0,50,'red')
light_off(0,0)
light_off(0,-50)

hideturtle()
exitonclick()
