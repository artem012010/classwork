from turtle import *
dali = Turtle() 
dali.shape('circle')
dali.pensize(5)

def draw(x,y):
    dali.goto(x,y)

def move(x,y):
    dali.penup()
    dali.goto(x,y)
    dali.pendown()

def setRed():
    dali.color('red')

def setBlack():
    dali.color('black')

def goUp():
    dali.goto(dali.xcor(),dali.ycor() + 5)

def goDown():
    dali.goto(dali.xcor(),dali.ycor() - 5)

def goLeft():
    dali.goto(dali.xcor() - 5,dali.ycor())

def goRight():
    dali.goto(dali.xcor() + 5,dali.ycor())

screen = dali.getscreen()
screen.listen()
screen.onscreenclick(move)
screen.onkey(setRed,'r')
screen.onkey(setBlack,'b')
screen.onkey(goUp,'w')
screen.onkey(goDown,'s')
screen.onkey(goLeft,'a')
screen.onkey(goRight,'d')
dali.ondrag(draw)
