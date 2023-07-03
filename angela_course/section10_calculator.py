
# def format_name(f_name, l_name):
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   return formated_f_name + ' ' + formated_l_name;

# print(format_name("angela", "ANGELA"))


# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         print("Leap year.")
#         return True
#       else:
#         return False

#     else:
#       return True
#   else:
#     return False

# # docstring
# def days_in_month(year, month):
# #  """returns days of year.month"""
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#   if is_leap(year):
#       return month_days[month] + 1
#   else:
#       return month_days[month]  
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month-1)
# print(days)



# calculator

def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mul(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2

operation = {
  "+" : add, 
  "-" : sub, 
  "/" : div,  
  "*" : mul,
}

num1 = int(input("What's the first number?: "))

for op in operation:
  print(op)

continue_calc = True

while continue_calc:
  operation_symbol=input("Pick an opeation: ")
  num2 = int(input("What's the next number?: "))
  answer = operation[operation_symbol](num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  if input(f"Type 'y' to continue calculating with {answer}: ") == 'y':
    num1 = answer
  else:
    continue_calc = False

  
