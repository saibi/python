logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcom to the secret auction program!")

players = []

continue_game = True
while continue_game:
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  another = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  user = {}
  user["name"] = name
  user["bid"] = bid
  players.append(user)
  
  if another == "no":
    continue_game = False

high_bidder = {}
high_value = 0
for player in players:
  if high_value < player["bid"]:
    high_value = player["bid"]
    high_bidder = player

print(f'The winner is {high_bidder["name"]} with a bid of ${high_bidder["bid"]}')
