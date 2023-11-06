from turtle import *
 
speed(10)

def kvadrat(storona, cvet):
    color(cvet)
    begin_fill()
    for i in range(4):
        forward(storona)
        left(90)
    end_fill()

kvadrat(125,'black')
kvadrat(100,'white')
kvadrat(75,'gray')
kvadrat(50,'black')


hideturtle()
exitonclick()
