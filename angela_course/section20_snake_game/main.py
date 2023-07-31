from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

turtle_size = 20

screen.tracer(0)
starting_positions = [(0, 0), (-turtle_size, 0), (-turtle_size*2, 0)]
segments = []
for i in range(3):
    turtle = Turtle("square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(starting_positions[i])
    segments.append(turtle)

screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments)-1, 0, -1):
        pos = segments[seg_num-1].position()
        segments[seg_num].goto(pos)

    segments[0].forward(turtle_size)


screen.exitonclick()
