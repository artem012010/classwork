from turtle import *

class Sprite(Turtle):
    def __init__(self,x,y,col,shp):
        super().__init__()
        self.penup()
        self.goto(x,y)
        self.color(col)
        self.shape(shp)

player = Sprite(0,-100,'black','turtle')
enemy1 = Sprite(-100,-50,'red','circle')
enemy2 = Sprite(100,50,'red','circle')
goal = Sprite(0,100,'green','triangle')
