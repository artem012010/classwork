from turtle import *

sergey = Turtle()
sergey.shape('circle')
sergey.size = 0

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

def beginFill():
    sergey.begin_fill()

def endFill():
    sergey.end_fill()

def cClear():
    sergey.clear()

def penMinus():
    sergey.size -= 1
    sergey.pensize(sergey.size)

def penPlus():
    sergey.size += 1
    sergey.pensize(sergey.size)

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
screen.onkey(beginFill,'q')
screen.onkey(endFill,'e')
screen.onkey(cClear,'c')
screen.onkey(penPlus,'i')
screen.onkey(penMinus,'o')
