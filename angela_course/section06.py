fruits=[ "Apple", "Peach", "pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")


# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


sum = 0
count = 0

#Write your code below this row 👇
for item in student_heights:
    sum += item
    count += 1

print(int(round(sum/count, 0)))



# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max_score = 0
for score in student_scores:
  if score > max_score:
    max_score = score

print(f"The highest score in the class is: {max_score}")



sum = 0
for value in range(2, 101, 2):
    sum += value

print(sum)


for value in range(1, 101):
  if value % (3*5) == 0:
    print("FizzBuzz")
  elif value % 3 == 0:
    print("Fizz")
  elif value % 5 == 0:
    print("Buzz")
  else:
    print(value)



str=[]

for val in range(1, nr_letters+1):
  str.append(letters[random.randint(0, len(letters) -1)])

for val in range(1, nr_numbers+1):
  str.append(numbers[random.randint(0, len(numbers) -1)])

for val in range(1, nr_symbols+1):
  str.append(symbols[random.randint(0, len(symbols) -1)] )

pw = ''
for a in range(0, len(str)):
  pw += str.pop(random.randint(0, len(str) -1))

print(pw)

#random.choice()
#random.shuffle()


  


