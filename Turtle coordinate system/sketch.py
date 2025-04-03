import turtle

tim = turtle.Turtle()
screen = turtle.Screen()

def forward():
    tim.forward(20)

def backwards():
    tim.backward(20)

def left():
    tim.setheading(tim.heading()+10)

def right():
    tim.setheading(tim.heading() - 10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(forward, "w")
screen.onkey(backwards, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(clear, "c")

screen.mainloop()
