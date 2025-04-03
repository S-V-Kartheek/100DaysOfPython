import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#creating screen
screen=turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
#Making objects
food=Food()
snake=Snake()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

flag=True
while flag:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect Collision with food
    if snake.head.distance(food)<15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset()
        time.sleep(0.5)
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            flag=False
            scoreboard.reset()
            snake.reset()

screen.exitonclick()