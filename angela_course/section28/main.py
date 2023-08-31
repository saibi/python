from tkinter import *
import math
from timeit import default_timer as timer

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps, timer

    window.after_cancel(timer)
    reps = 0
    label_title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    label_check.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps

    reps += 1

    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
        label_title.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        if reps % 8 == 0:
            count_down(LONG_BREAK_MIN * 60)
            label_title.config(text="Break", fg=RED)
            reps = 0
        else:
            count_down(SHORT_BREAK_MIN * 60)
            label_title.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps, timer
    canvas.itemconfig(
        timer_text, text=f"{math.floor(count/60) :02d}:{count%60 :02d}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        label_check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


label_title = Label(text="Timer", fg=GREEN, bg=YELLOW,
                    font=(FONT_NAME, 40, "bold"))
label_title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", bg=YELLOW,
                      highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", bg=YELLOW,
                      highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

label_check = Label(text="✓", fg=GREEN, bg=YELLOW,
                    font=(FONT_NAME, 20, "bold"))
label_check.grid(column=1, row=3)


window.mainloop()
