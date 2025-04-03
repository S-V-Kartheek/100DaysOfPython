import turtle
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time
import winsound  # For sound effects (Windows only)

# Screen Setup
screen = turtle.Screen()
screen.title("Pong Game 🎯")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Game Elements
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Keyboard Controls
screen.listen()
screen.onkeypress(r_paddle.paddle_up, "Up")
screen.onkeypress(r_paddle.paddle_down, "Down")
screen.onkeypress(l_paddle.paddle_up, "w")
screen.onkeypress(l_paddle.paddle_down, "s")

# Game Loop
game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Ball collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
       
    # Ball collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # Ball went out of screen right side
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_score()
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    # Ball out of screen left side
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_score()
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    # Check for Winner
    if scoreboard.left_score == 3:
        scoreboard.display_winner("Left")
        game_on = False
    elif scoreboard.right_score == 3:
        scoreboard.display_winner("Right")
        game_on = False

# Exit on Click
screen.exitonclick()
