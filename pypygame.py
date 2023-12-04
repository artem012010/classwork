from turtle import *

class Sprite(Turtle):
    def __init__(self,x,y,step,shape,color):
        super().__init__()
        self.penup()
        self.shape(shape)
        self.color(color)
        self.goto(x,y)
        self.step = step

    def move_up(self):
        self.goto(self.xcor(),self.ycor() + self.step )
    def move_down(self):
        self.goto(self.xcor(),self.ycor() - self.step )
    def move_left(self):
        self.goto(self.xcor() - self.step,self.ycor())
    def move_right(self):
        self.goto(self.xcor() + self.step,self.ycor())

screen = pirat.getscreen()
screen.listen()

screen.onkey(pirat.move_up,'Up')
screen.onkey(pirat.move_down,'Down')
screen.onkey(pirat.move_left,'Left')
screen.onkey(pirat.move_right,'Right')
