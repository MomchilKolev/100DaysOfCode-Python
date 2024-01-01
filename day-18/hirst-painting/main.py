# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('spot-painting.webp', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
from turtle import Turtle, Screen, colormode
import random

tom = Turtle()

color_list = [
    (233, 233, 232),
    (231, 233, 238),
    (237, 231, 234),
    (224, 233, 227),
    (207, 160, 82),
    (55, 88, 130),
    (145, 91, 40),
    (139, 27, 49),
    (221, 207, 108),
    (133, 176, 202),
    (157, 47, 84),
    (44, 54, 104),
    (169, 159, 41),
    (129, 189, 144),
    (83, 20, 44),
    (38, 43, 66),
    (185, 94, 106),
    (188, 139, 165),
    (86, 119, 179),
    (59, 39, 31),
    (89, 156, 91),
    (80, 153, 164),
    (194, 81, 72),
    (160, 201, 219),
    (79, 75, 43),
    (45, 75, 78),
    (55, 123, 120),
    (46, 75, 74),
    (217, 176, 188),
    (169, 207, 165),
]

colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_hirst_painting(turtle):
    turtle.up()
    turtle.hideturtle()
    x_start = -280
    y_start = -240
    print(turtle.pos())
    for y in range(0, 10):
        turtle.sety(y * 50 + y_start)
        for x in range(1, 11):
            turtle.setx(x * 50 + x_start)
            turtle.dot(20, random_color())

screen = Screen()
draw_hirst_painting(tom)

screen.exitonclick()