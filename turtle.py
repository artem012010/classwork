from turtle import *

sergey = Turtle()
sergey.shape('circle')

def draw(x,y):
    sergey.goto(x,y)

def move(x,y):
    sergey.penup()
    sergey.goto(x,y)
    sergey.pendown()

def setGreen():
    sergey.color('green')

def setBlack():
    sergey.color('black')

def goUp():
    sergey.goto(sergey.xcor(),sergey.ycor() + 5)
def goDown():
    sergey.goto(sergey.xcor(),sergey.ycor() - 5)
def goRight():
    sergey.goto(sergey.xcor() + 5,sergey.ycor())
def goLeft():
    sergey.goto(sergey.xcor() - 5,sergey.ycor())

sergey.ondrag(draw)
screen = sergey.getscreen()
screen.listen()
screen.onscreenclick(move)
screen.onkey(setGreen,'g')
screen.onkey(setBlack,'b')
screen.onkey(goUp,'Up')
screen.onkey(goDown,'Down')
screen.onkey(goRight,'Right')
screen.onkey(goLeft,'Left')
