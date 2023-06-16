/*
import random
import my_module

print(my_module.pi)

random_integer = random.randint(1, 2)
print(random_integer)

random_float = random.random()
print(random_float)


random_int = random.randint(1,2)
if random_int == 1:
  print("Heads")
else:
  print("Tails")



states_of_america = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']


# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
str = names_string.replace(" ", "")
names = str.split(",")

vote = random.randint(0, len(names) - 1)
print(f"{names[vote]} is going to buy the meal today!")

*/

/*
# 🚨 Don't change the code below 👇
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
val = int(position)
col = int(val / 10) - 1
row = val % 10 - 1
map[row][col] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
*/



import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

img = [ rock, paper, scissors]

you = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

print(img[you]);

print("Computer chose:")
com = random.randint(0, 2)
print(img[com])

judge = [ [0, -1, 1 ], [1, 0 , -1], [ -1, 1, 0]]
result = judge[you][com]
if result == 1:
  print("You win")
elif result == -1:
  print("You loose")
else:
  print("tie")



