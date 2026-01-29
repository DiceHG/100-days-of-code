from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.shapesize(0.75, 0.75)
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)
    
    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)
    