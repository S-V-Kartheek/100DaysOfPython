import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
# registers the image shape
screen.addshape(image)
#applies the image as the turtles appearance
turtle.shape(image)

# to load state data
data=pandas.read_csv("50_states.csv")
all_states=data["state"].to_list()
guessed_states=[]

# Game loop
while len(guessed_states) < 50:
    guess = screen.textinput(f"{len(guessed_states)}/50  states correct", "Whats the state name?").title()

    if guess=="Exit":
        missed_states=[state for state in all_states if state not in guessed_states]

        new_data=pandas.DataFrame(missed_states)
        new_data.to_csv("states to learn.csv",header=["Missed states"])
        print("Missed states saved to 'states_to_learn.csv'")
        break

    if guess in all_states:
        guessed_states.append(guess)
        # creating turtle for writing state names on image
        timmy=turtle.Turtle()
        timmy.penup()
        timmy.hideturtle()
        state_data=data[data.state==guess]

        nx,ny=state_data.x.item(), state_data.y.item()

        timmy.goto(nx,ny)
        timmy.write(f"{guess}",align="center",font=("Arial", 8, "bold"))

# display message when all states are guessed
if len(guessed_states)==50:
    turtle.clearscreen()
    screen.title("Congratulations! You guessed all 50 states! 🎉")
    turtle.write("You guessed all states!", align="center", font=("Arial", 20, "bold"))
