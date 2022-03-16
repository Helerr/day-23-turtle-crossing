from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 250)
        self.write("Level: 1", font=FONT, align="left")

    def game_over(self):
        self.goto(-100, 0)
        self.write("GAME OVER!", font=FONT, align="left")