from turtle import *
from time import *

def light(x,y,col,enabled):
    if enabled:
        color(col)
        penup()
        goto(x,y)
        pendown()
        begin_fill()
        circle(30)
        end_fill()
    else:
        color(col)
        penup()
        goto(x,y)
        pendown()
        circle(30)

def ramka():
    color('black')
    penup()
    goto(-50,120)
    pendown()
    forward(80)
    right(90)
    forward(200)
    right(90)
    forward(80)
    right(90)
    forward(200)
    right(90)

while True:
    ramka()
    light(0,65,'red',True)
    light(0,0,'yellow',False)
    light(0,-65,'green',False)
    sleep(5)
    clear()
    ramka()
    light(0,65,'red',False)
    light(0,0,'yellow',True)
    light(0,-65,'green',False)
    sleep(5)
    clear()
    ramka()
    light(0,65,'red',False)
    light(0,0,'yellow',False)
    light(0,-65,'green',True)
    sleep(5)
    clear()


hideturtle()
exitonclick()
