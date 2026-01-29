from turtle import Turtle

class FinishLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("red")
        self.pensize(3)
        self.penup()
        self.goto(-300, 240)
        self.pendown()
        self.goto(300, 240)