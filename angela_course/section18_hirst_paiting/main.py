# "$ conda install cologram" => no package error
# just do "$ pip install colorgram.py" in conda env
#
# import colorgram


# def to_color_tuple(spot_color):
#     return (spot_color.rgb.r, spot_color.rgb.g, spot_color.rgb.b)


# spot_colors = colorgram.extract('spot.jpeg', 30)
# print(spot_colors)
# colors = []
# for i in spot_colors:
#     colors.append(to_color_tuple(i))

# print(colors)

import turtle
import random

turtle.colormode(255)

t = turtle.Turtle()

color_list = [(248, 248, 246), (247, 232, 241), (227, 238, 247), (235, 247, 242), (238, 224, 81), (205, 4, 74), (199, 164, 8), (238, 48, 132), (206, 75, 12), (109, 180, 219), (218, 161, 104), (235, 224, 4), (28, 190, 109), (11, 24, 64), (20,
                                                                                                                                                                                                                                              107, 176), (15, 28, 178), (218, 133, 179), (7, 186, 216), (228, 167, 200), (211, 24, 151), (120, 191, 159), (7, 50, 26), (60, 21, 7), (125, 219, 234), (32, 136, 71), (192, 13, 4), (108, 88, 215), (141, 217, 202), (238, 63, 35), (69, 10, 27)]

t.speed("fastest")

t.hideturtle()


def draw_circle(radius, color):
    t.dot(radius, color)
    # t.fillcolor(color)
    # t.begin_fill()
    # t.circle(radius)
    # t.end_fill()


def move_right(distance):
    t.penup()
    t.forward(distance)
    t.pendown()


def move_up(distance):
    t.penup()
    t.left(90)
    t.forward(distance)
    t.right(90)
    t.pendown()


def return_to_left(distance):
    t.penup()
    t.backward(distance)
    t.pendown()


def goto_start_pos():
    t.penup()
    t.backward(space * width/2)
    t.right(90)
    t.forward(space * height / 2)
    t.left(90)
    t.pendown()


width = 10
height = 10
dot_size = 20
space = 50


goto_start_pos()

for j in range(height):
    for i in range(width):
        draw_circle(dot_size, random.choice(color_list))
        move_right(space)

    move_up(space)
    return_to_left(space * width)


screen = turtle.Screen()
screen.exitonclick()
