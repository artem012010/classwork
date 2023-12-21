from turtle import *

def light(x,y,col,on):
    penup()
    goto(x,y)
    pendown()
    color(col)
    if on:
        begin_fill()
        circle(30)
        end_fill()
    else:
        circle(30)

light(x=0,y=60,col='red',on=True)
light(x=0,y=0,col='yellow',on=False)
light(x=0,y=-60,col='green',on=False)


hideturtle()
exitonclick()
