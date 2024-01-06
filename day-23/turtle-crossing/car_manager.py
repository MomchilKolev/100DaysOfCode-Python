import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEFT_EDGE = -300


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.create_car(0)

    def create_car(self, level):
        # more cars as level increases otherwise they are too sparse
        random_chance = random.randint(0, 6) + round(level / 2)
        if random_chance > 5:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(self.random_position())
            self.cars.append(new_car)

    @staticmethod
    def random_position():
        return 250, random.randint(-250, 250)

    def move(self):
        for car in self.cars:
            car.forward(self.move_speed)
            if car.xcor() < LEFT_EDGE:
                car.hideturtle()
                self.cars = self.cars[1:]

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
