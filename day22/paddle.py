from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos_x):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(pos_x, 0)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)