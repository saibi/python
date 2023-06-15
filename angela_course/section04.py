#!/usr/bin/python3 

/*
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm ? "))

if height > 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")
*/

# exercise #1 

number = int(input("Which number do you want to check? "));
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")


# exercise #2
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / (height*height))

if bmi < 18.5:
  interpretation="you are underweight"
elif bmi <25:
  interpretation = "you have a normal weight"
elif bmi < 30:
  interpretation = "you are slightly overweight"
elif bmi < 35:
  interpretation = "you are obese"
else:
  interpretation = "you are clinically obese"

print(f"Your BMI is {bmi}, {interpretation}.")


# exercise #3
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
      print("Leap year.")
else:
  print("Not leap year.")


#exercise #4
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == 'S':
  bill = 15
  if add_pepperoni == 'Y':
    bill += 2
elif size == 'M':
  bill = 20
  if add_pepperoni == 'Y':
    bill += 3
else:
  bill = 25
  if add_pepperoni == 'Y':
    bill += 3

if extra_cheese == 'Y':
  bill += 1

print(f"Your final bill is: ${bill}.")

#exercise #5
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0

total += name1.lower().count('t');
total += name1.lower().count('r');
total += name1.lower().count('u');
total += name1.lower().count('e');
total += name2.lower().count('t');
total += name2.lower().count('r');
total += name2.lower().count('u');
total += name2.lower().count('e');

total2 = 0
total2 += name1.lower().count('l');
total2 += name1.lower().count('o');
total2 += name1.lower().count('v');
total2 += name1.lower().count('e');

total2 += name2.lower().count('l');
total2 += name2.lower().count('o');
total2 += name2.lower().count('v');
total2 += name2.lower().count('e');

score = total * 10 + total2

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


# final
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

answer1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()

if answer1 == "left":
  answer2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
  if answer2 == "swim":
    answer3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? \n").lower()
    if answer3 == "red":
      print("It's a room full of fire. Game Over.")
    elif answer3 == "blue":
      print("You found the treasure! You Win!")
    elif answer3 == "yellow":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")


