import pandas as pd
import turtle
from state_manager import StateManager


data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

def find_state(state):
    state = data[data.state == state]
    if state.empty:
        return None
    return state.head(1).squeeze()


state_manager = StateManager()

answer_list = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(
        title=f"{len(answer_list)}/{len(all_states)} Guess the State", prompt="What's another state's name?")

    if answer_state is None:
        game_is_on = False
        continue

    answer_state = answer_state.title()

    state = find_state(answer_state)
    if state is not None:
        print(state)
        state_manager.add_state(
            state["state"], int(state["x"]), int(state["y"]))
        answer_list.append(answer_state)

learn = list(set(all_states) - set(answer_list))
print(learn)

d = pd.DataFrame(learn)
d.to_csv("learn.csv")


# screen.exitonclick()
