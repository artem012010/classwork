from turtle import *

gena = Turtle() # Создаем обьект Черепашки
gena.shape('circle')

#функция для обработки перетаскивания
def move(x,y):
    gena.goto(x,y)

#функция для обработки клика по экрану
def click_screen(x,y):
    gena.penup()
    gena.goto(x,y)
    gena.pendown()

screen = gena.getscreen() # Создаем обьект экрана
#Подписка на клик по экрану
screen.onscreenclick(click_screen)
#Подписка на перетаскивание черепашки
gena.ondrag(move)
