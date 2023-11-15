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
