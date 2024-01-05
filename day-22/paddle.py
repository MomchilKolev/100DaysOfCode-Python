from turtle import Turtle
DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.x_pos = position[0]
        self.y_pos = position[1]
        self.create_paddle()

    def create_paddle(self):
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.x_pos, self.y_pos)

    def go_up(self):
        new_y = self.ycor() + DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - DISTANCE
        self.goto(self.xcor(), new_y)
