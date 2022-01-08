from turtle import Turtle, Screen, turtles
import random
import turtle
screen = Screen()
is_race_on=False
user_bet= screen.textinput(title="Mack youre bet",prompt="which turtle will win the race?Enter the color: ")
colors = ["red", "green", "blue", "pink", "yellow","orange"]
direction = [-70, -40, -10, 20, 50, 80]
screen.setup(width=500, height=400)
all_turtle=[]
for index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=direction[index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"you've won!! . The {winning_color} turtle is the winner.")
            else:
                print(f"You've Lost!!. The {winning_color} turtle is the winner.")


        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
