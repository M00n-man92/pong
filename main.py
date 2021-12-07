from turtle import *
from paddle import Paddle
from secpad import Sec
from turtle import Turtle
from ball import Ball
from score import Score_Board
import time
is_game_on=True
pad=Paddle()
sec=Sec()


screen=Screen()
screen.tracer(0)
ball=Ball()
time.sleep(0.01)
screen.setup(800,600)
screen.bgcolor("black")
screen.listen()
screen.onkey(pad.move_up,"Up")
screen.onkey(pad.move_doen,"Down")
screen.onkey(sec.move_doen,"space")
screen.onkey(sec.move_up,"w")
sec.left_pad()
pad.right_pad()
lscore=Score_Board(lpos=-70,rpos=270)
rscore=Score_Board(lpos=70,rpos=270)
for i in range(1,30):
    if i%2==0:
        tur=Turtle()
        tur.color("white")
        tur.shape("square")
        tur.turtlesize(stretch_wid=0.9,stretch_len=0.1)
        tur.setposition(0,-300+(i*20))
    else:
        tur=Turtle()
        tur.color("black")
        tur.shape("square")
        tur.turtlesize(stretch_wid=0.9,stretch_len=0.1)
        tur.setposition(0,-300+(i*20))

while lscore.le_count<=10 and rscore.ri_count<=10 and is_game_on:
    time.sleep(0.03)
    
    screen.update()
    
    ball.move()
    if ball.xcor()<=370 and ball.xcor()>=-370 :
        
        
        if ball.ycor()>=270 or ball.ycor()<=-270:
            
            ball.minus()
           
        
        elif ball.xcor()==340 or ball.xcor()==-340:
            
            
            if ball.distance(pad)<50 or ball.distance(sec)<50:
                
                ball.linus()
    elif ball.xcor()==380:
        lscore.le_count+=1
        lscore.left()
        time.sleep(1)
        ball.rset()
        
        
    elif ball.xcor()==-380:
        rscore.ri_count+=1
        
        rscore.right()
        time.sleep(1)
        ball.rset()   

                       
        

        
    # else:
    #     if score.le_count==10 or score.ri_count==10:
    #         is_game_on=False



# for i in range(1,30):
#     turtle=Turtle()
#     turtle.shape("square")
#     turtle.penup()
#     turtle.color("white")
#     turtle.setheading(90)
    
    
#     turtle.goto(0,-300+(i*20))
#     turtle.penup()
#     turtle.hideturtle()
#     turtle.forward(20)
#     turtle.pendown()
#     turtle.showturtle()
#     turtle.forward(20)


    # turtle.penup()
    # turtle.forward(20)
    # turtle.pen
    # turtle.

screen.exitonclick()


screen.listen()