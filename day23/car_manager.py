from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.goto(280, (random.randint(-11, 11) * 20) + 5)
        self.setheading(180)

class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Car()
        self.cars.append(car)

    def move(self, player):
        for index, car in enumerate(self.cars):
            car.forward(self.move_distance)
            if abs(car.xcor() - player.xcor()) < 22 and car.ycor() - player.ycor() == 5:
                return False
            if car.xcor() < -340:
                del self.cars[index]
        return True
    
    def speedup(self):
        self.move_distance += MOVE_INCREMENT

    