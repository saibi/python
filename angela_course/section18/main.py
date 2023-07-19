# from turtle import Turtle, Screen
# import random

# tim = Turtle()

# tim.shape("turtle")
# tim.color("red", "green")

# square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# colors = ["red", "orange", "brown", "yellow", "green", "turquoise", "blue", "violet", "pink", "gray", "black" ]

# def draw_shape(num_sides):
#     if 360 % num_sides != 0:
#         return

#     angle = int(360 / num_sides)
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape in range(3, 11):
#     print(f"shape {shape}")
#     tim.color(random.choice(colors))
#     draw_shape(shape)

import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()

# direction= [0,90, 180, 270]
# def random_walk(distance):
#     new_color = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
#     tim.color(new_color)
#     tim.setheading(random.choice(direction))
#     tim.forward(distance)

# tim.width(10)
# tim.speed("fastest")
# for _ in range(100):
#     random_walk(20)


tim.speed("fastest")
step = 5
for _ in range(0, 360, step):
    new_color = (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    tim.color(new_color)
    tim.circle(100)
    tim.right(step)


screen = turtle.Screen()
screen.exitonclick()
