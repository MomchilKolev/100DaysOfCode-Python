from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.setheading(90)
        self.penup()
        self.restart()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.restart()
            return True
        return False

    def restart(self):
        self.goto(STARTING_POSITION)