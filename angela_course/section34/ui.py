from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 250


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label_score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.canvas = Canvas(width=CANVAS_WIDTH,
                             height=CANVAS_HEIGHT, bg="white")
        self.question = self.canvas.create_text(
            CANVAS_WIDTH/2, CANVAS_HEIGHT/2, text="question area", fill=THEME_COLOR, font=FONT, width=CANVAS_WIDTH-20)
        image_true = PhotoImage(file="images/true.png")
        image_false = PhotoImage(file="images/false.png")
        self.button_true = Button(
            image=image_true, highlightthickness=0, command=self.true_pressed)
        self.button_false = Button(
            image=image_false, highlightthickness=0, command=self.false_pressed)

        self.label_score.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        self.button_true.grid(row=2, column=0)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            q_text = self.quiz.get_next_question()
            self.canvas.itemconfig(self.question, text=q_text)
            self.label_score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(
                self.question, text="You've reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
