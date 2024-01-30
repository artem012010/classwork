from turtle import *

class Sprite(Turtle):
    def __init__(self,x,y,col,shp):
        super().__init__()
        self.penup()
        self.left(90)
        self.goto(x,y)
        self.color(col)
        self.shape(shp)

    def collide(self,sprite):
        dist = self.distance(sprite.xcor(),sprite.ycor())
        if dist < 30:
            return True
        else:
            return False

    def move_up(self):
        self.goto(self.xcor(),self.ycor()+5)
    def move_down(self):
        self.goto(self.xcor(),self.ycor()-5)
    def move_right(self):
        self.goto(self.xcor()+5,self.ycor())
    def move_left(self):
        self.goto(self.xcor()-5,self.ycor())

    def set_move(self, xs,ys,xe,ye):
        self.xs = xs
        self.ys = ys
        self.xe = xe
        self.ye = ye
        self.goto(xs,ys)
        self.setheading(self.towards(xe,ye))

    def make_step(self):
        self.forward(10)
        if self.distance(self.xe,self.ye) < 10:
            self.set_move(self.xe,self.ye,self.xs,self.ys)

player = Sprite(0,-200,'black','turtle')
enemy1 = Sprite(-100,-50,'red','circle')
enemy1.set_move(-100,-50,100,-50)
enemy2 = Sprite(100,50,'red','circle')
enemy2.set_move(100,50,-100,50)
goal = Sprite(0,100,'green','triangle')

screen = player.getscreen()
screen.listen()

screen.onkey(player.move_up,'w')
screen.onkey(player.move_down,'s')
screen.onkey(player.move_right,'d')
screen.onkey(player.move_left,'a')

points = 0

while points < 3:
    enemy1.make_step()
    enemy2.make_step()
    if player.collide(goal):
        player.goto(0,-200)
        points += 1
    if player.collide(enemy1) or player.collide(enemy2):
        goal.hideturtle()
        break

if points == 3:
    enemy1.hideturtle()
    enemy2.hideturtle()
    player.hideturtle()
    goal.hideturtle()
    goal.goto(-100,-50)
    goal.write('Победа',font=('Arial',50,'bold'))
