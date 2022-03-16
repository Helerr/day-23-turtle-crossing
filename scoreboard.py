from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 250)
        self.level = 1
        self.display_level()

    def game_over(self):
        self.goto(-100, 0)
        self.write("GAME OVER!", font=FONT, align="left")

    def update_level(self):
        self.level += 1
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT, align="left")
