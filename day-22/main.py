from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.update()
screen.listen()
# screen.tracer(1)
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with ball
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # Detect collision with paddle
    if ((ball.distance(r_paddle) <= 50 and ball.xcor() > 320) or ball.distance(l_paddle) <= 50 and
            ball.xcor() < -320):
        ball.bounce_x()

    # Detect when right paddle misses
    elif ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when left paddle misses
    elif ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

# screen.exitonclick()
