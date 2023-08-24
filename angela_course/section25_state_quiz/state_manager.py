from turtle import Turtle
FONT = ("Courier", 16, "normal")


class StateManager():
    def __init__(self):
        self.states = []

    def add_state(self, name, x, y):
        new_state = Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(x, y)
        new_state.write(name, align="center", font=FONT)
        self.states.append(new_state)
