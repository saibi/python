from tkinter import *
from tkinter import PhotoImage

import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

word_dict = {}
word = None
id_after = None


def load_words():
    global word_dict
    try:
        data = pd.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        data = pd.read_csv("data/korean_words.csv")
    finally:
        word_dict = {row.English: row.Korean for (
            index, row) in data.iterrows()}
        # to_learn = data.to_dict(orient="records")
        print(word_dict)


load_words()


def next_word():
    global word, id_after
    word = random.choice(list(word_dict.keys()))
    canvas_front.itemconfig(background_image, image=image_front)
    canvas_front.itemconfig(text_title, text="English", fill="black")
    canvas_front.itemconfig(text_word, text=word, fill="black")
    if id_after != None:
        window.after_cancel(id_after)
    id_after = window.after(3000, flip)


def remove_word():
    word_dict.pop(word)
    new_data = pd.DataFrame(word_dict.items(), columns=["English", "Korean"])
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


def flip():
    canvas_front.itemconfig(background_image, image=image_back)
    canvas_front.itemconfig(text_title, text="Korean", fill="white")
    canvas_front.itemconfig(text_word, text=word_dict[word], fill="white")


window = Tk()
window.title("flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas_front = Canvas(width=800, height=526,
                      bg=BACKGROUND_COLOR, highlightthickness=0)
image_front = PhotoImage(file="images/card_front.png")
background_image = canvas_front.create_image(800/2, 526/2, image=image_front)
text_title = canvas_front.create_text(
    400, 150, text="English", font=TITLE_FONT)
text_word = canvas_front.create_text(400, 263, text="word", font=WORD_FONT)
image_back = PhotoImage(file="images/card_back.png")

image_right = PhotoImage(file="images/right.png")
image_wrong = PhotoImage(file="images/wrong.png")

button_right = Button(
    image=image_right, highlightthickness=0, command=remove_word)
button_wrong = Button(
    image=image_wrong, highlightthickness=0, command=next_word)

canvas_front.grid(column=0, row=0, columnspan=2)
button_right.grid(column=1, row=1)
button_wrong.grid(column=0, row=1)

next_word()

window.mainloop()
