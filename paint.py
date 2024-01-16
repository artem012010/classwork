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

#функция для обработки клавиши g
def green_color():
    gena.color('green')

#функция для обработки клавиши Стрелка вверх
def moveUp():
    gena.goto(gena.xcor(),gena.ycor()+5)

screen = gena.getscreen() # Создаем обьект экрана
screen.listen() # Просим экран слушать клавиатуру
screen.onkey(green_color,'g') # Подписка на клавишу g
screen.onkey(moveUp,'Up') # Подписка на клавишу Стрелка
#Подписка на клик по экрану
screen.onscreenclick(click_screen)
#Подписка на перетаскивание черепашки
gena.ondrag(move)
