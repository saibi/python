logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
  cipher_text = ""
  for ch in text:
    cipher_index = (alphabet.index(ch) + shift) % len(alphabet)
    cipher_text += alphabet[cipher_index]   

  print(f"The encoded text is {cipher_text}")

def decrypt(cipher, shift):
  plain_text = ""
  for ch in cipher:
    plain_index = ( alphabet.index(ch) - shift + len(alphabet) ) % len(alphabet)
    plain_text += alphabet[plain_index]

  print(f"The decoded text is {plain_text}")

# if direction == "encode":
#   encrypt(text, shift)
# else:
#   decrypt(text, shift)

def caesar(start_text, shift_amount, direction):
  end_text = ""
  if direction != "encode":
    shift_amount *= -1
    
  for ch in start_text:
    try:
      alpha_index = alphabet.index(ch)
      new_index = (alpha_index + shift_amount + len(alphabet)) % len(alphabet)
      end_text += alphabet[new_index]   
    except ValueError: 
      end_text += ch

  print(f"The {direction}d text is {end_text}")

def game():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text, shift, direction)

  
print(logo)

continue_game = True
while continue_game:
  game()
  answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
  if answer != "yes":
    continue_game = False
