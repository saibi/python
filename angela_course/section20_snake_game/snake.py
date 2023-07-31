from turtle import Turtle

SEGMENT_SIZE = 20
STARTING_POSITIONS = [(0, 0), (-SEGMENT_SIZE, 0), (-SEGMENT_SIZE*2, 0)]


class Snake:

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(pos)
            self.segments.append(turtle)

    def move(self) -> None:
        for seg_num in range(len(self.segments)-1, 0, -1):
            pos = self.segments[seg_num-1].position()
            self.segments[seg_num].goto(pos)

        self.segments[0].forward(SEGMENT_SIZE)
