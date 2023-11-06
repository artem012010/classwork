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








from turtle import*
pensize(2)
goto(-50,-50)

def square ():
    for i in range(4):
        forward(200)
        left(90)

begin_fill()
square()    
end_fill() 

penup()
goto(170,-50)
pendown()
begin_fill()
circle(3)
end_fill() 
hideturtle()
exitonclick()

