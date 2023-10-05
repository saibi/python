import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def get_next_question(self):
        self.current_question = self.question_list[self.question_number]
        q_text = html.unescape(self.current_question.text)
        self.question_number += 1
        return f"Q.{self.question_number}: {q_text}"

    def next_question(self):
        user_answer = input(f"{self.get_next_question()} (True/False): ")
        self.check_answer(user_answer)

    def check_answer(self, user_answer) -> bool:
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            ret = True
        else:
            print("That's wrong.")
            ret = False

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
        return ret
