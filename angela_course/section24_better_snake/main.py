from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True


def game_over():
    # restart
    scoreboard.reset()
    snake.reset()

    # exit
    # global game_is_on
    # game_is_on = False
    # scoreboard.game_over()


while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect food
    if snake.head.distance(food) < 18:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over()

    # detect tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over()

screen.exitonclick()
