from turtle import Turtle
class Score_Board(Turtle):
    def __init__(self,lpos,rpos) :
        super().__init__()
        self.le_count=0
        self.ri_count=0
        self.color("white")
        self.penup()
        self.goto(lpos,rpos)
        self.hideturtle()
               
        self.write(arg=f"{self.le_count}",align="center",font=('Arial', 17, 'normal'))

    def left(self):
        
        
        # if self.le_count>0:
        
        self.clear()        
        self.write(arg=f"{self.le_count}",align="center",font=('Arial', 17, 'normal'))
        
            
        
        
        
    def right(self):
        
        self.clear()
        self.write(arg=f"{self.ri_count}",align="center",font=('Arial', 17, 'normal'))
        
            