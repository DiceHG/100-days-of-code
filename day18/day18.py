import turtle as t
import random

# import colorgram

# colors = colorgram.extract('./painting.jpg', 30)
# colors_tuples = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
# colors_tuples = colors_tuples[4:]
# print(colors_tuples)

t.colormode(255)

colors = [(208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165)]

turtle = t.Turtle()
turtle.speed(5)
turtle.pu()

for i in range(10):
    for j in range(9):
        x = -200 + 50 * j
        y = -200 + 50 * i
        turtle.goto(x, y)
        turtle.dot(20, random.choice(colors))

turtle.hideturtle()

screen = t.Screen()
screen.exitonclick()