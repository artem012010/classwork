from turtle import *
from time import *
from random import *

adolf = Turtle()
adolf.color('blue')
adolf.shape('turtle')
adolf.penup()
adolf.points = 0

def poimali(x,y):
    adolf.write('ВАЙ?',font=('Arial',20,'normal'))
    adolf.points += 1
    adolf.goto(randint(-200,200),randint(-200,200))

adolf.onclick(poimali)

while adolf.points < 3:
    adolf.goto(randint(-200,200),randint(-200,200))
    sleep(1)

adolf.clear()
adolf.goto(-100,-50)
adolf.write('Ты победил',font=('Arial',30,'bold'))
adolf.hideturtle()




# ВТОРАЯ ВЕРСИЯ
from turtle import *
from time import *
from random import *

adolf = Turtle()
iosif = Turtle()
vladimir = Turtle()

def start(name,col,angle):
    name.color(col)
    name.shape('turtle')
    name.penup()
    name.left(angle)

start(adolf,'black',0)
start(iosif,'yellow',120)
start(vladimir,'red',240)

def poimali_gitlera(x,y):
    adolf.goto(randint(-30,30),randint(-30,30))
    adolf.left(randint(0,360))

def poimali_stalina(x,y):
    iosif.goto(randint(-30,30),randint(-30,30))
    iosif.left(randint(0,360))

def poimali_lenina(x,y):
    vladimir.goto(randint(-30,30),randint(-30,30))
    vladimir.left(randint(0,360))


def finish(adolf,iosif,vladimir):
    adolf_out = abs(adolf.xcor()) > 200 or abs(adolf.ycor()) > 200 
    iosif_out = abs(iosif.xcor()) > 200 or abs(iosif.ycor()) > 200 
    vladimir_out = abs(vladimir.xcor()) > 200 or abs(vladimir.ycor()) > 200 
    itog = adolf_out or iosif_out or vladimir_out 
    return itog 

adolf.onclick(poimali_gitlera)
iosif.onclick(poimali_stalina)
vladimir.onclick(poimali_lenina)

start = time()
while finish(adolf,iosif,vladimir) == False:
    adolf.forward(5)
    iosif.forward(5)
    vladimir.forward(5)
end = time()

adolf.goto(-150,-50)
adolf.write('Ты продержался ' + str(int(end-start)) + ' с',font=('Arial',25,'bold'))
adolf.hideturtle()
iosif.hideturtle()
vladimir.hideturtle()


