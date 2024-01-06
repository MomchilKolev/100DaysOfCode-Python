import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create a turtle player that starts at the bottom of the screen and
# listen for the "Up" keypress to move the turtle north. If you get
# stuck, check the video walkthrough in Step 3.
player = Player()
screen.listen()
screen.onkey(fun=player.go_up, key="Up")

# Create cars that are 20px high by 40px wide that are randomly generated
# along the y-axis and move to the left edge of the screen. No cars should
#  be generated in the top and bottom 50px of the screen (think of it as a
#  safe zone for our little turtle). *Hint*: generate a new car only
#  every 6th time the game loop runs. If you get stuck, check the video
#  walkthrough in Step 4.
car_manager = CarManager()

# Create a scoreboard that keeps track of which level the user is on.
# Every time the turtle player does a successful crossing, the level
# should increase. When the turtle hits a car, GAME OVER should be
# displayed in the centre. If you get stuck, check the video walkthrough
# in Step 7.
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()

    # New car
    car_manager.create_car(scoreboard.level)

    # Detect when the turtle player collides with a car and stop the game if
    # this happens. If you get stuck, check the video walkthrough in Step 5.
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when the turtle player has reached the top edge of the screen
    # (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle
    # to the starting position and increase the speed of the cars.
    # *Hint*: think
    #  about creating an attribute and using the MOVE_INCREMENT to increase
    # the car speed. If you get stuck, check the video walkthrough in Step 6.
    if player.at_finish_line():
        scoreboard.next_level()
        car_manager.increase_speed()


screen.exitonclick()
