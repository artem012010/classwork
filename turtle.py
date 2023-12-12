from turtle import *
pensize(2)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
exitonclick()


from turtle import *

pensize(10)
color("blue")
forward(100)

exitonclick() 

from turtle import *

pensize(15)
color('lightblue')

forward(100)
left(120)
forward(100)
left(120)
forward(100)

exitonclick()


from turtle import *

pensize(10)

color('pink')
circle(50)

color('orange')
circle(50)

color('yellow')
circle(50)

color('lime')
circle(50)

exitonclick()


from turtle import *
 
def ship():
  color('light blue')
  pensize(5)
  forward(50)
  left(180-45)
  forward(70)
  left(180-45)
  forward(50)
  color('black')
  pensize(2)
  forward(30)
  right(90)
  forward(45)
  left(180-45)
  forward(50)
  left(45)
  forward(80)
  left(45)
  forward(50)
  left(180-45)
  forward(105)
    
 
#отрисовка волны, не менять
penup()
goto(-110,-25)
pendown()
color("blue")
pensize(2)
left(45)
speed(0)
i=0
while i<20:
   forward(10)
   right(90)
   forward(10)
   left(90)
   i=i+1
right(45)
 
#отрисовка кораблика
penup()
goto(0,-30)
pendown()
ship() 

right(180)
penup()
goto(-130,130)
pendown()
ship()

right(180)
penup()
goto(130,130)
pendown()
ship()

exitonclick()

