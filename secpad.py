from turtle import Turtle
class Sec(Turtle):
    def __init__(self):
        super().__init__()
    def left_pad(self):
        self.penup()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.setpos(-350,0)
    def move_up(self):
                
        self.goto(self.xcor(),self.ycor()+20) 
    def move_doen(self):
        

        self.goto(self.xcor(),self.ycor()-20)       