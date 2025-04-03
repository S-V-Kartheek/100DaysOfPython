from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars_list=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def generate_cars(self):
        work=random.randint(1,5)
        if work==1:
            timmy=Turtle()
            timmy.shape("square")
            timmy.turtlesize(1,2)
            timmy.color(random.choice(COLORS))
            timmy.setheading(180)
            timmy.penup()
            new_y=random.randint(-250,250)
            timmy.goto(300,new_y)
            self.cars_list.append(timmy)

    def move_cars(self):
        for car in self.cars_list:
            car.forward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed+=MOVE_INCREMENT

