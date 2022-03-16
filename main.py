import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()
game_is_on = True

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
obstacles = []
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_down, "Down")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20 and (player.ycor() < (car.ycor() + 10) or player.ycor() > (car.ycor - 10)):
            scoreboard.game_over()
            game_is_on = False

    #Detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.update_level()

screen.exitonclick()