from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed(0)
        self.goto(random.randint(-28, 28) * 10, random.randint(-28, 28) * 10 + 5)

    def refresh(self):
        self.goto(random.randint(-28, 28) * 10, random.randint(-28, 28) * 10 + 5)