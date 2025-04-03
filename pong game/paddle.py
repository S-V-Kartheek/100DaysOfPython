from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def paddle_up(self):
        if self.ycor() < 250:  # Upper boundary limit
            self.goto(self.xcor(), self.ycor() + 30)

    def paddle_down(self):
        if self.ycor() > -250:  # Lower boundary limit
            self.goto(self.xcor(), self.ycor() - 30)
