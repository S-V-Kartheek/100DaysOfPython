import turtle
import random
import time

screen=turtle.Screen()
screen.setup(width=600,height=500)
screen.title("Turtle Racing Game 🏁🐢")
screen.bgcolor("lightblue")
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: (crimson, deepskyblue, limegreen, gold, orchid, tomato)")

# Drawing End Line
tom=turtle.Turtle()
tom.teleport(280,-200)
tom.setheading(90)
tom.pensize(4)
tom.forward(400)
tom.hideturtle()

# creating tuples and setting there positions
turtle_list=[]
colors = ["crimson", "deepskyblue", "limegreen", "gold", "orchid", "tomato"]

y_position=[-100,-50,0,50,100,150]
for i in range(0,6):
    timmy=turtle.Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[i])
    timmy.goto(-280,y_position[i])
    turtle_list.append(timmy)

# Start Race Countdown
screen.tracer(0)  # Disable animation for countdown effect
countdown_turtle = turtle.Turtle()
countdown_turtle.hideturtle()
countdown_turtle.penup()
countdown_turtle.goto(0, 180)
for count in ["3", "2", "1", "Go!"]:
    countdown_turtle.clear()
    countdown_turtle.write(count, align="center", font=("Arial", 24, "bold"))
    screen.update()
    time.sleep(1)

countdown_turtle.clear()
screen.tracer(1)  # Re-enable animation

if user_bet in colors:
    flag=True

while flag:
    for turtle in turtle_list:
        turtle.forward(random.randint(1,10))
        # checking which turtle has won
        if turtle.xcor()>280:
            flag=False
            winner_color=turtle.pencolor()

            if user_bet==winner_color:
                print(f"You've won!The {winner_color} has won the game")
            else:
                print(f"You've lose!The {winner_color} has won the game")


screen.exitonclick()
