from turtle import *

adolf = Turtle()
adolf.color('black')

iosif = Turtle()
iosif.color('red')
iosif.left(90)

naruto = Turtle()
naruto.color('orange')
naruto.left(180)

donatello = Turtle()
donatello.color('violet')
donatello.left(270)

for i in range(120):
    adolf.forward(3)
    iosif.forward(3)
    naruto.forward(3)
    donatello.forward(3)
    adolf.left(3)
    iosif.left(3)
    naruto.left(3)
    donatello.left(3)





from turtle import *
from random import *

rafaelo = Turtle()
leonardo = Turtle()

def start_race(name,col,x,y):
    name.color(col)
    name.shape('turtle')
    name.penup()
    name.goto(x,y)

def dance(name):
    name.goto(0,0)
    name.pendown()
    name.circle(50)

start_race(rafaelo,'red',-200,40)
start_race(leonardo,'blue',-200,-40)

while rafaelo.xcor() < 200 and leonardo.xcor() < 200:
    rafaelo.forward( randint(5,20) )
    leonardo.forward( randint(5,20) )

if max(rafaelo.xcor(),leonardo.xcor()) == rafaelo.xcor():
    dance(rafaelo)
elif max(rafaelo.xcor(),leonardo.xcor()) == leonardo.xcor():
    dance(leonardo)
