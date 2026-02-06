import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

df = pd.read_csv("50_states.csv")

states_list = df["state"].to_list()
correct_guesses = []

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

while len(correct_guesses) != 50:
    guess = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()

    if guess in states_list and guess not in correct_guesses:
        correct_guesses.append(guess)
        state, x, y = df[df["state"] == guess].values[0]
        pen.goto(x, y)
        pen.write(state)

    if guess == "Q":
        break

    screen.update()

df = pd.DataFrame(list(set(states_list) - set(correct_guesses)))
df.to_csv("missing_states.csv", index=False, header=False)