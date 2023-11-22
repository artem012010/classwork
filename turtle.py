from turtle import *

sergey = Turtle()
sergey.shape('circle')

def draw(x,y):
    sergey.goto(x,y)

def move(x,y):
    sergey.penup()
    sergey.goto(x,y)
    sergey.pendown()

sergey.ondrag(draw)
screen = sergey.getscreen()
screen.onscreenclick(move)
