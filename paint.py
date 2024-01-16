from turtle import *

gena = Turtle() 
gena.shape('circle')
gena.size = 1

def drag(x,y):
    gena.goto(x,y)

def click(x,y):
    gena.penup()
    gena.goto(x,y)
    gena.pendown()

def yellowCol():
    gena.color('yellow')

def blackCol():
    gena.color('black')

def moveUp():
    gena.goto(gena.xcor(),gena.ycor() + 5)

def moveDown():
    gena.goto(gena.xcor(),gena.ycor() - 5)

def moveRight():
    gena.goto(gena.xcor() + 5,gena.ycor())

def moveLeft():
    gena.goto(gena.xcor() - 5,gena.ycor())

def plusSize():
    gena.size += 1
    gena.pensize(gena.size)

def minusSize():
    gena.size -= 1
    gena.pensize(gena.size)

def beginFill():
    gena.begin_fill()

def endFill():
    gena.end_fill()

screen = gena.getscreen() 
screen.onscreenclick(click)
screen.listen() 

screen.onkey(yellowCol,'y')
screen.onkey(blackCol,'b')

screen.onkey(moveUp,'Up')
screen.onkey(moveDown,'Down') 
screen.onkey(moveRight,'Right') 
screen.onkey(moveLeft,'Left') 

screen.onkey(plusSize,'o') 
screen.onkey(minusSize,'p') 

screen.onkey(beginFill,'q') 
screen.onkey(endFill,'w') 

gena.ondrag(drag)
