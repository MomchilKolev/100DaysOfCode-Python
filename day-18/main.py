from turtle import Turtle, Screen, color, colormode
import random

tim = Turtle()
tim.shape('turtle')
tim.color('magenta')
# Turtle Challenge 1 - Square
# for n in range(4):
#     tim.forward(100)
#     tim.left(90)

# Turtle Challenge 2 - Dashed line
# for n in range(40):
#     if n % 2 == 0:
#         tim.up()
#     else:
#         tim.down()
#     tim.forward(10)

# Turtle Challenge 3 - Different shapes
# Each side is 100
# Each shape is different random color
# overlayed on top of each other
# colormode(255)
# def change_color(turtle):
#     R = random.randint(0, 255)
#     B = random.randint(0, 255)
#     G = random.randint(0, 255)

#     turtle.color(R, G, B)

# def draw_shape(turtle, num_sides):
#     for side in range(num_sides):
#         tim.forward(100)
#         tim.right(360 / num_sides)

# for sides in range(3, 11):
#     change_color(tim)
#     draw_shape(tim, sides)

# Turtle Challenge 4 - Random walk
# random walk of same distance
# different colors
# thicker lines
# faster drawing

colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def walk(turtle):
    turtle.left(random.choice([90, 180, 270, 360]))
    turtle.forward(50)
    turtle.color(random_color())

# tim.pensize(10)
# tim.speed(6)

# for n in range(1000):
#     walk(tim)

# Turtle Challenge 5 - Draw a Spirograph
def draw_spirograph(num_of_circles, circle_size):
    for n in range(0, num_of_circles):
        tim.circle(circle_size)
        tim.left(360/num_of_circles)
        tim.color(random_color())

tim.speed('fastest')

draw_spirograph(100, 100)

screen = Screen()
screen.exitonclick()