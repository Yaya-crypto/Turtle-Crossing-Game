import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(fun=player.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Player advances to next level
    if player.ycor() >= 280:
        player.reset()
        scoreboard.update_level()
        car_manager.increase_speed()

    # Player hit a car
    for cars in car_manager.all_cars:
        if player.distance(cars) < 22:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
