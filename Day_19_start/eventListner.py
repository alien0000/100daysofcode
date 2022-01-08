from turtle import Turtle,Screen
tim=Turtle()




def move():
    tim.forward(20)
screen=Screen()

screen.listen()
screen.onkey(key="space",fun=move)
screen.exitonclick()
