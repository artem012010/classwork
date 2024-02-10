Ответы на задания

Задание 1. «Ваш уют: оформление комнат»
1.1. Правильные варианты ответов:


1.4. Программа:
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


1.5. Программа :
from turtle import *
pensize(10)
color("blue")
forward(100)
exitonclick() 


1.6. Программа:
from turtle import *
color("light blue")
pensize(15)
forward(100)
left(120)
forward(100)
left(120)
forward(100)
exitonclick()

1.7. Программа:
from turtle import *
pensize(10)
color("pink")
circle(50)
color("orange")
circle(50)
color("yellow")
circle(50)
color("lime")
circle(50)
exitonclick()


Доп задание 1.1. Правильный ответ:





Доп задание 1.2. Программа:
from turtle import *
pensize(2)
color("green")
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)


left(90)
color("yellow")
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)
exitonclick()


Доп задание 1.3. Верные утверждения:


Задание 2. «Ваш уют: оформление комнат 2»

2.1. Правильные варианты ответов:
	


2.3.  Программа:
from turtle import *
a = 100
b = 90
pensize(2)
forward(a)
left(b)
forward(a)
left(b)
forward(a)
left(b)
forward(a)
exitonclick()


2.4.  Программа:
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
goto(0,50)
pendown()
ship()
exitonclick()

2.5. Программа:
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


penup()
goto(0,-30)
pendown()
ship()
penup()
goto(130,130)
pendown()
right(180)
ship()
penup()
goto(-130,130)
pendown()
right(180)
ship()
exitonclick()

Доп задание 2.1


from turtle import *
pensize(2)
color("black")
begin_fill()
circle(60)
end_fill()
penup()


color("red")
goto(100,100)
pendown()
begin_fill()
circle(20)
end_fill()
penup()


color("green")
goto(-100,-100)
pendown()
begin_fill()
circle(30)
end_fill()
penup()


color("blue")
goto(-100,100)
pendown()
begin_fill()
circle(40)
end_fill()
penup()


color("yellow")
goto(100,-100)
pendown()
begin_fill()
circle(80)
end_fill()


exitonclick()


Доп задание 2.2
from turtle import *
def square():
   pensize(2)
   forward(100)
   left(90)
   forward(100)
   left(90)
   forward(100)
   left(90)
   forward(100)
   left(90)


color("pink")
left(15)
square()
left(15)
square()
left(15)
square()
left(15)
square()
left(15)
square()
exitonclick()




Дополнительное задание «Трек 3»
1.1. Верные ответы:
	


1.2. Программа:
from turtle import *
pensize(2)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(30)
forward(50)
right(120)
forward(50)
right(120)
exitonclick()


1.3. Программа:
from turtle import *
pensize(2)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)


exitonclick()


1.4. Программа:
from turtle import *
pensize(5)
forward(100)
left(90)
forward(150)
left(90)
forward(100)
left(90)
forward(150)


pensize(2)
left(90)
forward(50)
left(90)
forward(150)
left(90)
forward(50)


left(90)
forward(75)
left(90)
forward(100)


exitonclick()


1.5. Программа:
from turtle import *
pensize(5)
forward(100)
left(90)
forward(150)
left(90)
forward(100)
left(90)
forward(150)


penup()
goto(80,80)
pendown()
circle(5)


exitonclick()






Ответы на задания

Задание 1. «Министерство культуры: задачи»
1.1. Правильные варианты ответов:


1.3. Программа:
from turtle import *
pensize(2)
for i in range(4):
   forward(100)
   left(90)
hideturtle()
exitonclick()


1.4. Программа :
from turtle import *
pensize(2)
for i in range(5):
    forward(100)
    left(72)
hideturtle()
exitonclick()


1.5. Программа:
from turtle import *
penup()
goto(-200, 0)
pendown()
pensize(10)


for i in range(4):
    color("indigo")
    left(70)
    forward(50)
    right(140)
    forward(50)
    left(140)
    color("thistle")
    forward(100)
    right(140)
    forward(100)
    left(70)
hideturtle()
exitonclick()


1.6. Программа:
from turtle import *


def triangle():
    pensize(2)
    color("blue")
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)
speed(10)
for i in range(36):
    triangle()  
    right(10)
hideturtle()
exitonclick()




Доп. задание 1.1. Правильный ответ:



Доп. задание 1.2. Программа:

from turtle import *
pensize(2)
speed(10)
color("navy")
size = 10
for i in range(7):
   circle(size)
   size = size+10
left(90)
color("navy")
size = 10
for i in range(7):
   circle(size)
   size = size+10
left(90)
color("navy")
size = 10
for i in range(7):
   circle(size)
   size = size+10
left(90)
color("navy")
size = 10
for i in range(7):
   circle(size)
   size = size+10 
hideturtle()
exitonclick()

Задание 2. «Министерство культуры: задачи 2»

2.1. Правильные варианты ответов:
	


2.2.  Программа:
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


2.3.  Программа:
	from turtle import*
goto(-50, -50)
def square(length, cur_color):
   pensize(2)
   color(cur_color)
   begin_fill()
   for i in range(4):
       forward(length)
       left(90)
   end_fill()
square(200, 'black')   
square(150, 'white')
square(100, 'lavender')
square(50, 'black')
hideturtle()
exitonclick()

2.4. Программа:
from turtle import*
def star ():
    pensize(2)
    color("darkblue")
    i=0
    begin_fill()
    while i<5:
        forward(150)
        left(144)
        i=i+1
    end_fill()
star()
hideturtle()     
exitonclick()  


2.5. Программа:
from turtle import*
def sun ():
    pensize(2)
    color("yellow")
    i=0
    begin_fill()
    while i<18:
        forward(150)
        left(100)
        i=i+1
    end_fill()
sun()     
hideturtle()
exitonclick() 

Доп. задание 2.1





Доп. задание 2.2
from turtle import*
def star ():
    pensize(2)
    color("darkblue")
    i=0
    begin_fill()
    while i<5:
        forward(50)
        left(144)
        i=i+1
    end_fill()
speed(10)
coordinate_x =- 200
coordinate_y =- 100
for i in range(5):
    penup()
    goto(coordinate_x,coordinate_y)
    pendown()
    star()    
    coordinate_x += 80
    coordinate_y += 50
hideturtle()
exitonclick()   


Дополнительное задание «Министерство культуры: доп задания»
3.1. Верные ответы:
	


3.2. Программа:
from turtle import *
pensize(3)
speed(10)
length = 10
for i in range(25):
    forward(length)
    length += 10
    left(90)
hideturtle()
exitonclick()


3.3. Программа:
	from turtle import *
def square1():
    color('black','white')
    pendown()
    begin_fill()
    for i in range(4):
        forward(50)
        left(90)  
    end_fill()   
def square2():
    color('black')
    pendown()
    begin_fill()
    for i in range(4):
        forward(50)
        left(90)  
    end_fill()        
pensize(2)
penup()
goto(-200,50)
for i in range(4):
   square2()
   forward(50)
   square1()
   forward(50)
penup()
goto(-200,0)   
for i in range(4):
   square1()
   forward(50)
   square2()
   forward(50)
penup()
goto(-200,-50)
for i in range(4):
   square2()
   forward(50)
   square1()
   forward(50)
hideturtle()
exitonclick()




Ответы на задания

Задание 1. «Полиция: задачи»
1.1. Правильное соответствие:


1.2.  Текст программы без ошибок.

from turtle import *
def star ():
    pensize(2)
    color("red")
    begin_fill()
    for i in range(5):
        forward(100)
        left(144)
    end_fill()    
star()
hideturtle()    
exitonclick()

1.3. Текст программы:

from turtle import *
pensize(2)
color("red")
begin_fill()
circle(50)
end_fill()
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

1.4. Текст программы:

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



Бонус 1. Правильный вариант ответа:


Бонус 2. Текст программы:
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

Задание 2. «Полиция: задачи 2»
2.1. Правильное соответствие:


2.2. Текст программы:
	from turtle import *


def fence_link():
    pensize(2)
    color("black","orange")
    begin_fill()
    left(90)
    forward(100)
    right(30)
    forward(42)
    right(120)
    forward(42)
    right(30)
    forward(100)
    right(90)
    forward(42)
    left(180)
    end_fill()


penup()
goto(-150,0)
pendown()
for i in range(6):
    fence_link()
    forward(42)
 
hideturtle()
exitonclick()



2.3.  Текст программы:
from turtle import *
def fence(color_f):
    color(color_f)
    pensize(3)
    penup()
    goto(-215, 0)
    pendown()
    for i in range(4):
        left(90)
        forward(50)
        right(90)
        forward(25)
        left(90)
        forward(50)
        right(90)
        forward(25)
        right(90)
        forward(50)
        left(90)
        forward(25)
        right(90)
        forward(50)
        left(90)
        forward(25)
        
answer = input("Введи корпус: главный корпус/приёмная жителей")
if answer == "главный корпус":
    fence("blue")
if answer == "приёмная жителей":    
    fence("green")
hideturtle()
exitonclick()

2.4. Текст программы:

from turtle import *
def red_light_on():
    color("red")
    penup()
    goto(0,100)
    pendown()
    begin_fill()
    circle(35)
    end_fill()
def red_light_off():
    color("red")
    penup()
    goto(0,100)
    pendown()
    circle(35)
def yellow_light_on():
    color("yellow")
    penup()
    goto(0,0)
    pendown()
    begin_fill()
    circle(35)
    end_fill()
def yellow_light_off():
    color("yellow")
    penup()
    goto(0,0)
    pendown()
    circle(35)
def green_light_on():
    color("green")
    penup()
    goto(0,-100)
    pendown()
    begin_fill()
    circle(35)
    end_fill()
def green_light_off():
    color("green")
    penup()
    goto(0,-100)
    pendown()
    circle(35)
answer = input("Какой горит цвет красный/жёлтый/зелёный?")
if answer == "красный":
    red_light_on()
    yellow_light_off()
    green_light_off()
if answer == "жёлтый":
    red_light_off()
    yellow_light_on()
    green_light_off()
if answer == "зелёный":
    red_light_off()
    yellow_light_off()
    green_light_on()
hideturtle()
exitonclick()

Бонус 1. Текст программы:

from turtle import *
penup()
goto(0,-150)
pendown()
color("brown")
pensize(20)
left(90)
forward(200)


pensize(10)
length = 10
color("green")
for i in range(26):
    forward(length)
    length = length + 5
    left(90)
hideturtle()
exitonclick()    


Дополнительное задание «Полиция: доп задачи»

1.1. Правильное соответствие:


1.2. Программа без ошибок:

from turtle import*
def pizza():
    color("black","orange")
    begin_fill()
    left(60)
    forward(160)
    right(108)
    forward(100)
    right(108)
    forward(160)
    end_fill()


def pepperoni():
    begin_fill()
    color("black","salmon")
    circle(10)
    end_fill()


pensize(2)
penup()
goto(-50,-30)
pendown()
pizza()
penup()
goto(-10,15)
pendown()
pepperoni()
penup()
goto(45,40)
pendown()
pepperoni()
penup()
goto(20,65)
pendown()
pepperoni()


hideturtle()
exitonclick()

1.3. Текст программы:

from turtle import*
pensize(15)
color("red")
circle(70)


penup()
goto(-35,45)
pendown()
color("black")
write("60",font=('Arial', 50, 'normal'))


hideturtle()
exitonclick()




Ответы на задания

Файл 1. «Модуль city» — должен быть опубликован в «Лаборатории»
from turtle import *


def draw_landscape():
   penup()
   goto(-200, -200)
   pendown()
   color('green', 'yellowgreen')
   begin_fill()
   for i in range(2):
       forward(400)
       left(90)
       forward(100)
       left(90)
   end_fill()


def draw_sky():
   penup()
   goto(-200, -100)
   pendown()
   #color('paleturquoise')
   color('skyblue')
   begin_fill()
   for i in range(2):
       forward(400)
       left(90)
       forward(300)
       left(90)
   end_fill()


def draw_window():
   color('yellow')
   begin_fill()
   for i in range(4):
       forward(20)
       left(90)  
   end_fill() 


def draw_block_of_flats():
   penup()
   goto(-170, -170)
   pendown()
   color('black', 'gray')
   begin_fill()
   for i in range(2):
       forward(100)
       left(90)  
       forward(200)
       left(90)
   end_fill()
   penup()
   goto(-145, -145)
   pendown()
   draw_window()
   penup()
   goto(-115, -145)
   pendown()
   draw_window()
   penup()
   goto(-145, -85)
   pendown()
   draw_window()
   penup()
   goto(-115, -85)
   pendown()
   draw_window()
   penup()
   goto(-145, -35)
   pendown()
   draw_window()
   penup()
   goto(-115, -35)
   pendown()
   draw_window()


def draw_sun():
   penup()
   goto(140, 140)
   pendown()
   begin_fill()
   color('orange', 'yellow')
   for i in range(18):
       forward(40)
       left(100)
   end_fill()


def draw_pharmacy():
   penup()
   goto(120, -160)
   pendown()
   color('brown', 'goldenrod')
   begin_fill()
   for i in range(3):
       forward(70)
       left(90)  
   end_fill()
   penup()
   goto(140, -110)
   pendown()
   pensize(5)
   color('red')
   forward(15)
   penup()
   goto(150, -118)
   pendown()
   color('red')
   right(90)
   forward(20)

Файл 2. «Основная программа» — должен быть опубликован в «Лаборатории»
	
import city


speed(0)
city.draw_landscape()
city.draw_sky()
city.draw_block_of_flats()
city.draw_sun()
city.draw_pharmacy()


hideturtle()
exitonclick()
