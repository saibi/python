from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


COLLISION_X = 330
PADDLE_X = 380

game_is_on = True
while game_is_on:
    ball.move()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >= COLLISION_X or ball.distance(l_paddle) < 50 and ball.xcor() <= -COLLISION_X:
        ball.bounce()

    # detect paddle miss
    if ball.xcor() > PADDLE_X:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -PADDLE_X:
        ball.reset_position()
        scoreboard.r_point()

    screen.update()
    time.sleep(ball.move_speed)

screen.exitonclick()
