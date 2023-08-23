from turtle import Turtle

FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = 0

        self.load_data()

        self.penup()
        self.color("white")
        self.speed("fastest")
        self.ht()
        self.goto(0, 270)
        self.update_scoreboard()

    def load_data(self):
        try:
            with open("data.txt") as f:
                data = f.read()
            self.high_score = int(data)
        except FileNotFoundError:
            pass

    def save_data(self, value):
        with open("data.txt", "w") as f:
            f.write(f"{value}")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center",
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_data(self.high_score)
        self.score = 0
        self.update_scoreboard()
