from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto((-200, 250))
        self.hideturtle()
        self.write_score()

    def next_level(self):
        self.level += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"LEVEL: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)

