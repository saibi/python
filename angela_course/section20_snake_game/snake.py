from turtle import Turtle

SEGMENT_SIZE = 20
STARTING_POSITIONS = [(0, 0), (-SEGMENT_SIZE, 0), (-SEGMENT_SIZE*2, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(pos)
        self.segments.append(turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self) -> None:
        for seg_num in range(len(self.segments)-1, 0, -1):
            pos = self.segments[seg_num-1].position()
            self.segments[seg_num].goto(pos)

        self.head.forward(SEGMENT_SIZE)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
