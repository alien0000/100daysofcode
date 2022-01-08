from turtle import Screen
from snack import Snack
from food import Food
from scorebord import Scorebord
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snack Game")
screen.tracer(0)


snack=Snack()
food=Food()
scorebord=Scorebord()

screen.listen()
screen.onkey(snack.up,"Up")
screen.onkey(snack.down,"Down")
screen.onkey(snack.left,"Left")
screen.onkey(snack.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snack.move()
        
    #Detect  collision with food.
    if snack.head.distance(food)<15:
        food.refrash()
        snack.extend()
        scorebord.increase_score()
    
    # Detect collision with wall.

    if snack.head.xcor()>280 or snack.head.xcor()<-280 or snack.head.ycor()>280 or snack.head.ycor()<-280:
        game_is_on=False
        scorebord.game_over()

    #Detect collision with tail.
    for seg in snack.segments:
        # if seg==snack.head:
        #     pass
        if snack.head.distance(seg[1:])<10:
            game_is_on=False
            scorebord.game_over()
    

screen.exitonclick()
