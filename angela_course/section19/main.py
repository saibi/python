from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_foraward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_counter_clockwise():
    tim.left(10)


def move_clockwise():
    tim.right(10)


def clear_drawing():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()


screen.listen()
screen.onkey(key="w", fun=move_foraward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
