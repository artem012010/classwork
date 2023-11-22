from turtle import *
dali = Turtle() 
dali.shape('circle')
dali.pensize(5)
screen = dali.getscreen()
def draw(x,y):
    dali.goto(x,y)
def move(x,y):
    dali.penup()
    dali.goto(x,y)
    dali.pendown()
dali.ondrag(draw)
screen.onscreenclick(move)
