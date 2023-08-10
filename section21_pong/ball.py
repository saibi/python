from turtle import Turtle

WALL_Y = 280
DEFAULT_MOVE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = DEFAULT_MOVE
        self.y_move = DEFAULT_MOVE
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        if self.ycor() >= WALL_Y or self.ycor() <= -WALL_Y:
            self.y_move = -self.y_move

    def bounce(self):
        self.x_move = -self.x_move
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce()
        self.move_speed = 0.1
