from turtle import *

class Sprite(Turtle):
    def __init__(self,x,y,col,shp):
        super().__init__()
        self.penup()
        self.left(90)
        self.goto(x,y)
        self.color(col)
        self.shape(shp)

    def move_up(self):
        self.goto(self.xcor(),self.ycor()+5)
    def move_down(self):
        self.goto(self.xcor(),self.ycor()-5)
    def move_right(self):
        self.goto(self.xcor()+5,self.ycor())
    def move_left(self):
        self.goto(self.xcor()-5,self.ycor())

player = Sprite(0,-100,'black','turtle')
enemy1 = Sprite(-100,-50,'red','circle')
enemy2 = Sprite(100,50,'red','circle')
goal = Sprite(0,100,'green','triangle')

screen = player.getscreen()
screen.listen()

screen.onkey(player.move_up,'w')
screen.onkey(player.move_down,'s')
screen.onkey(player.move_right,'d')
screen.onkey(player.move_left,'a')
