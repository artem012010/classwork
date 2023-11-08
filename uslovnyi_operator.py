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



from turtle import *
 
def speed_ok():
    color("green")
    begin_fill()
    circle(50)
    end_fill()
    
def speed_over():  
    color("red")
    penup()
    goto(0,-70)
    pendown()
    begin_fill()
    circle(18)
    end_fill()
 
    penup()
    goto(-10,-10)
    pendown()
    begin_fill()
    forward(20)
    left(80)
    forward(100)
    left(100)
    forward(55)
    left(100)
    forward(100)
    end_fill()  
 
speed = int(input("Введите скорость транспорта:"))
if speed <= 60:
    speed_ok()
if speed > 60:
    speed_over()    
hideturtle()
exitonclick()






from turtle import *
from time import sleep
pensize(2)

def light(x,y,col,on):
    if on:
        penup()
        goto(x,y)
        pendown()
        color(col)
        begin_fill()
        circle(40)
        end_fill()
    else:
        penup()
        goto(x,y)
        pendown()
        color(col)
        circle(40)

def ramka():
    color('black')
    penup()
    goto(-75,175)
    pendown()
    forward(150)
    right(90)
    forward(300)
    right(90)
    forward(150)
    right(90)
    forward(300)
    right(90)


while True:
    ramka()
    light(0,90,'red',True)
    light(0,0,'yellow',False)
    light(0,-90,'green',False)
    sleep(3)
    clear()
    ramka()
    light(0,90,'red',False)
    light(0,0,'yellow',True)
    light(0,-90,'green',False)
    sleep(3)
    clear()
    ramka()
    light(0,90,'red',False)
    light(0,0,'yellow',False)
    light(0,-90,'green',True)
    sleep(3)
    clear()

hideturtle()
exitonclick()


