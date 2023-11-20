from turtle import *
from random import randint
from time import sleep

oleg = Turtle()
oleg.shape('turtle')
oleg.color('blue')
oleg.speed(10)
oleg.penup()

def rand_move():
    oleg.goto(randint(-200,200), randint(-200,200))
# Определи функцию-обработчик catch(x, y), которая обработает клик по черепашке 
# (успешные клики копятся в свойстве t.points)
# Создай подписку на событие «клик по объекту-черепашке»
while True:
    rand_move()
    sleep(0.1)
    
