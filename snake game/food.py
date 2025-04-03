from turtle import Turtle
import random

# Using inheritance .inheriting turtle class to food class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("cyan")
        self.penup()
        self.turtlesize(0.5,0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x,y)
