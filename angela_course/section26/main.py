# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_numbers = [n**2 for n in numbers]
# print(squared_numbers)

# result = [n for n in numbers if n % 2 == 0]
# print(result)


# with open("file1.txt", "r") as file1:
#     lines1 = file1.readlines()

# numbers1 = [int(line.strip()) for line in lines1]

# with open("file2.txt", "r") as file2:
#     lines2 = file2.readlines()

# numbers2 = [int(line.strip()) for line in lines2]

# print(numbers1)
# print(numbers2)

# result = [n for n in numbers1 if n in numbers2]
# print(result)


# import random

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_score = {student: random.randint(1, 100) for student in names}

# print(students_score)

# passed_students = {key: score for (
#     key, score) in students_score.items() if score >= 60}

# print(passed_students)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split(" ")
# result = {word: len(word) for word in words}
# print(result)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }

# weather_f = {day: (c * 9 / 5 + 32) for (day, c) in weather_c.items()}
# print(weather_f)

import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

print(df)

dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(dict)

user_word = input("Enter a word: ")
nato = [dict[letter.upper()] for letter in user_word]
print(nato)
