from turtle import Turtle,Screen
import turtle
tim=Turtle()
# turtle.clear()

def clear_scareen():
    # tim.reset()
    tim.clear()
    tim.penup()
    tim.home()
    tim.pencolor()

def move_forward():
    tim.forward(20)
def move_backward():
    tim.backward(20)
def turn_left():
    # tim.left(10)
    current_position=tim.heading()+10
    tim.setheading(current_position)
def turn_right():
    # tim.right(10)
    current_position=tim.heading()-10
    tim.setheading(current_position)

screen=Screen()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="c",fun=clear_scareen)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.exitonclick()
