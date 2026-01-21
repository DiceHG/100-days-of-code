from snake import Snake
import turtle as t
import time

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")
screen.listen()

for _ in range(400):
    snake.move()
    screen.update()
    time.sleep(0.1)
