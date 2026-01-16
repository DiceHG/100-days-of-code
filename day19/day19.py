import turtle as t
from random import randint

screen = t.Screen()

bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: (red/orange/yellow/blue/magenta/purple)")

screen.bgcolor("slate gray")
screen.setup(width=1500, height=900)

colors = ["red", "orange", "yellow", "green", "blue", "magenta", "purple"]
turtles = []

for i in range(len(colors)):
    turtle = t.Turtle(shape="turtle")
    turtle.pu()
    turtle.speed("normal")
    turtle.color(colors[i])
    turtle.shapesize(3, 3, 9)
    turtle.goto(x=-700, y=-300 + 100*i)
    turtles.append(turtle)

winner = ""
is_race_on = False

if bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = randint(1, 10) * 8
        turtle.fd(rand_distance)

        if turtle.xcor() > 750:
            is_race_on = False
            winner = turtle.pencolor()
            break

if winner == bet:
    print(f"You've won! The {winner} turle is the winner!!!")
else:
    print(f"You've Lost! The {winner} turle is the winner!!!")