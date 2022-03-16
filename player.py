import turtle
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
MOVE_INCREMENT = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        if self.ycor() < 300:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_right(self):
        if self.xcor() < 290:
            self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def move_left(self):
        if self.xcor() > -290:
            self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def move_down(self):
        if self.ycor() > -290:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
