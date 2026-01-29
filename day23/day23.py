import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from finish_line import FinishLine

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
finish_line = FinishLine()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

game_is_on = True
count = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    game_is_on = car_manager.move(player)

    if player.ycor() > 240:
        player.reset()
        car_manager.speedup()
        scoreboard.score()
    
    if count == 5:
        car_manager.create_car()
        count = 0
    else:
        count += 1

scoreboard.game_over()

screen.exitonclick()