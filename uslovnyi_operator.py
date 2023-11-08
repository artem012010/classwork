from turtle import *

def star():
    pensize(2)
    color('red')
    begin_fill()
    for i in range(5):
        forward(100)
        left(144)
    end_fill()


star()     
hideturtle()
exitonclick()




from turtle import *
pensize(2)
#круг
color("red")
begin_fill()
circle(50)
end_fill()
# квадрат
goto(-32,37)
color("white")
begin_fill()
forward(65)
left(90)
forward(20)
left(90)
forward(65)
left(90)
forward(20)
end_fill()
hideturtle()
exitonclick()

