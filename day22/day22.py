from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

player = Paddle(-350)
opponent = Paddle(350)
scoreboard = Scoreboard()
ball = Ball()

is_game_on = True

screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_down, "Down")

while is_game_on:
    time.sleep(0.03)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if abs(ball.ycor() - opponent.ycor()) > 30:
        if ball.ycor() < opponent.ycor():
            opponent.go_down()
        else:
            opponent.go_up()
    
    if ball.distance(player) < 50 and ball.xcor() < -330 or ball.distance(opponent) < 50 and ball.xcor() > 330:
        ball.bounce_x()
        ball.speedup()
    
    if ball.xcor() > 390:
        ball.reset()
        scoreboard.player_point()
    elif ball.xcor() < -390:
        ball.reset()
        scoreboard.opponent_point()

    if scoreboard.player_score > 9 or scoreboard.opponent_score > 9:
        is_game_on = False

screen.exitonclick()