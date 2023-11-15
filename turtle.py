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
