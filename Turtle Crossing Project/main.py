import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player=Player()
carmanager=CarManager()
scoreboard=Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkeypress(player.move_forward,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.generate_cars()
    carmanager.move_cars()
        
    for car in carmanager.cars_list:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_is_on=False

    if player.player_is_at_finish_line():
        player.reset_position()
        carmanager.increase_car_speed()
        scoreboard.level_up()


screen.exitonclick()