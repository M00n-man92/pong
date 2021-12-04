from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.turtlesize(stretch_len=1,stretch_wid=1)
        self.color("white")
        self.y=10
        self.x=10
    def move(self):
        self.goto(self.xcor()+self.x,self.ycor()+self.y)
    def minus(self):
        self.y*=-1
        self.move()
    def linus(self):
        self.x*=-1
        self.move()           
    def rset(self):
        self.goto(0,0)
        self.y*=-1    