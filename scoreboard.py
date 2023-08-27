from turtle import Turtle

FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-225, 260)

    def display_level(self):
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def inc_level(self):
        self.level += 1
        self.clear()
        self.display_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align="center", font=FONT)
