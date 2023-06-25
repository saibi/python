import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = len(stages) - 1
print(f'lives {lives}')

chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')

disp = []
for i in chosen_word:
    disp += "_"

print(logo)

end_of_game = False

while not end_of_game:
    print(f"{' '.join(disp)}")
    print(stages[lives])
    guess = input("guess a letter: ").lower()

    if guess in disp:
        print(f"You've already guessed {guess}")
    else:
        match = False

        for i in range(0, len(chosen_word)):
            if disp[i] == '_' and chosen_word[i] == guess:
                disp[i] = guess
                match = True

        if match:
            if disp.count('_') == 0:
                print("You win!")
                end_of_game = True
        else:
            print(
                f"You guessed {guess}, that's not in the word. You lose a life."
            )
            lives -= 1
            if lives == 0:
                print(stages[lives])
                print("You lose")
                end_of_game = True

