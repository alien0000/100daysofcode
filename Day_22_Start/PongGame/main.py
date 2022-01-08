from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorebord import ScoreBord
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

ball=Ball()

scorebord=ScoreBord()


screen.listen()
screen.onkey(fun=r_paddle.go_up,key="Up")
screen.onkey(fun=r_paddle.go_down,key="Down")
screen.onkey(fun=l_paddle.go_up,key="w")
screen.onkey(fun=l_paddle.go_down,key="s")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    
    # collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.resetPosition()
        scorebord.l_point()
        
    if ball.xcor()<-380:
        ball.resetPosition()
        scorebord.r_point()

screen.exitonclick()