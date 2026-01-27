from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(45)
        self.ball_speed = 10

    def move(self):
        self.forward(self.ball_speed)
    
    def bounce_y(self):
        self.setheading(360 - self.heading())
    
    def bounce_x(self):
        self.setheading((180 - self.heading()) % 360)
    
    def reset(self):
        self.goto(0, 0)
        self.ball_speed = 10
        self.setheading((self.heading() + 180) % 360)

    def speedup(self):
        self.ball_speed += 1
        