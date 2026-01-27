from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.player_score = 0
        self.opponent_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.opponent_score, align="center", font=("Courier", 50, "normal"))

    def player_point(self):
        self.player_score += 1
        self.update_scoreboard()

    def opponent_point(self):
        self.opponent_score += 1
        self.update_scoreboard()