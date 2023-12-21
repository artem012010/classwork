from turtle import *
from time import sleep

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

while True:
    light(0,60,'red',True)
    light(0,0,'yellow',False)
    light(0,-60,'green',False)
    sleep(2)
    clear()
    light(0,60,'red',False)
    light(0,0,'yellow',True)
    light(0,-60,'green',False)
    sleep(2)
    clear()
    light(0,60,'red',False)
    light(0,0,'yellow',False)
    light(0,-60,'green',True)
    sleep(2)
    clear()

hideturtle()
exitonclick()
