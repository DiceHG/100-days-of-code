import turtle as t

turtle = t.Turtle()

def forward():
    turtle.fd(20)

def backward():
    turtle.bk(20)

def turn_right():
    turtle.right(15)

def turn_left():
    turtle.left(15)

def reset():
    turtle.reset()

screen = t.Screen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(reset, "c")
screen.listen()
screen.exitonclick()