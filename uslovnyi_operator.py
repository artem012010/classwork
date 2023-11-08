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




from turtle import *

def day():
    pensize(2)
    color("yellow")
    begin_fill()
    for i in range(18):
        forward(100)
        left(100)
    end_fill()
    
def night():
    pensize(2)
    color("bisque")
    begin_fill()
    circle(50)
    end_fill()
    
answer = input("Какое сейчас время суток (день/ночь)?")

if answer == "день":
    day()

if answer == "ночь":
    night()  
      
hideturtle()
exitonclick()

