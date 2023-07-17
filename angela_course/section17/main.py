# class User:
#     def __init__(self, user_id, username) -> None:
#         self.id =user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#         print(f"new user {self.id} {self.username} being created.")

#     def follow(self, user):
#         user.followers += 1
#         self.following += 1


# user_1 = User("001", "angela")
# print(user_1.id)
# user_2 = User("002", "super")

# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)

# print(user_2.followers)
# print(user_2.following)


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    obj = Question(item["text"], item["answer"])
    question_bank.append(obj)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.nex_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
