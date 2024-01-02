from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


# def move_forwards():
#     tom.forward(10)

# screen.listen()
# screen.onkey(key="space", fun=move_forwards)

# 179, Challenge: Make an Etch-A-Sketch App

def move(n):
    return lambda: tom.forward(n)

def turn(deg):
    return lambda: tom.left(deg)

def clear():
    tom.home()
    tom.reset()

screen.onkey(key="w", fun=move(10))
screen.onkey(key="s", fun=move(-10))
screen.onkey(key="a", fun=turn(10))
screen.onkey(key="d", fun=turn(-10))
screen.onkey(key="c", fun=clear)


screen.listen()
screen.exitonclick()