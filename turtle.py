from turtle import *
from random import *

def dance(name):
    name.goto(0,0)
    name.pendown()
    for i in range(5):
        name.forward(100)
        name.left(144)

def start_race(name,col,x,y):
    name.penup()
    name.shape('turtle')
    name.color(col)
    name.goto(x,y)

naruto = Turtle()
start_race(naruto,'orange',-200,50)

saske = Turtle()
start_race(saske,'blue',-200,-50)

while naruto.xcor() < 200 and saske.xcor() < 200 :
    naruto.forward( randint(10,20) )
    saske.forward( randint(10,20) )

winner = max(naruto.xcor(), saske.xcor())
if naruto.xcor() == winner:
    dance(naruto)
if saske.xcor() == winner:
    dance(saske)
