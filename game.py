from turtle import *
from time import *
from random import *

adolf = Turtle()
adolf.color('blue')
adolf.shape('turtle')
adolf.penup()

while True:
    adolf.goto(randint(-200,200),randint(-200,200))
    sleep(1)
