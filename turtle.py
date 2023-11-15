from turtle import *

donatelo = Turtle()
donatelo.color('violet')

rafaelo = Turtle()
rafaelo.color('red')
rafaelo.left(120)

leonardo = Turtle()
leonardo.color('blue')
leonardo.left(240)

for i in range(60):
    donatelo.forward(6)
    donatelo.left(6)
    rafaelo.forward(6)
    rafaelo.left(6)
    leonardo.forward(6)
    leonardo.left(6)








from turtle import *
from random import *

adolf = Turtle()
iosif = Turtle()

def start_race(x,y,col,name):
    name.shape('turtle')
    name.color(col)
    name.penup()
    name.goto(x,y)

def dance(name):
    name.goto(0,0)
    name.pendown()
    for i in range(10):
        name.circle(30)
        name.left(36)

start_race(-200,30,'black',adolf)
start_race(-200,-30,'red',iosif)

while adolf.xcor() < 200 and iosif.xcor() < 200:
    adolf.forward( randint(1,10) )
    iosif.forward( randint(1,10) )

adolf_result = adolf.xcor()
iosif_result = iosif.xcor()

winner = max(adolf_result,iosif_result) 

if winner == adolf_result:
    dance(adolf) 
if winner == iosif_result:
    dance(iosif)
