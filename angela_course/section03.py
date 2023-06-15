#!/usr/bin/python3
print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
percent = int(input("What percentage tip would you like to give? 10, 12, 15? "))
n = int(input("How many people to split the bill? "))

if bill.startswith("$"):
  bill_val = float(bill[1:])
else:
  bill_val = float(bill)


tip = bill_val * percent / 100
total = bill_val + tip;
pay = round(total / n, 2)
print(f"Each person should pay:${pay}")

