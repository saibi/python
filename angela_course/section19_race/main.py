from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
start_y = -100
for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.pu()
    tim.goto(x=-230, y=start_y)
    tim.pd()

    turtles.append(tim)
    start_y += 40

is_race_on = True

goal_x = 230

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

        if turtle.pos()[0] > goal_x:
            winner = turtle
            is_race_on = False

print(f"{winner.color()[0]} wins")
if user_bet == winner.color()[0]:
    print("You Win")
else:
    print("You Lose")


screen.exitonclick()
