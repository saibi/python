# FileNotFound
# with open("a.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["wrong_key"]

# IndexError
# a_list = [1, 2, 3]
# value = a_list[3]

# TypeError
# a_string = "string"
# value = a_string + 1


# try:
#     with open("a.txt") as file:
#         file.read()
#     a_list = [1, 2, 3]
#     value = a_list[3]
# except FileNotFoundError:
#     print("There was an error")
# except IndexError as msg:
#     print(f"index error {msg}")
# else:
#     print("Everything is fine")
#     content = file.read()
#     print(content)

# finally:


# height = float(input("Height: "))
# weight = int(input("Weight: "))
# if height > 300:
#     raise ValueError("Human height should not be over 3 meters")

# bmi = weight / (height ** 2)
# print(bmi)


# fruits = ["apple", "banana", "orange"]

# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         fruit = "Fruit"

#     print(fruit + " pie")

# make_pie(0)
# make_pie(4)
# make_pie(2)

# facebook_posts = [
#     {"Likes": 21, "Comments": 2},
#     {"Likes": 13, "Comments": 2, "Shares": 1},
#     {"Likes": 33, "Comments": 8, "Shares": 3},
#     {"Comments": 4, "Shares": 2},
#     {"Comments": 1, "Shares": 1},
#     {"Likes": 19, "Comments": 3}
# ]
# total_likes = 0
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post["Likes"]
#     except KeyError:
#         pass

# print(total_likes)

# import pandas
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

# while True:
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#         break
#     except KeyError:
#         print("Sorry, only letters please")
#         continue

# print(output_list)

import json

with open("a.txt", "r") as file:
    data = json.load(file)
    print(data)
