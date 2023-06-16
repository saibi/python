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
