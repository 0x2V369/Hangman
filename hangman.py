import random

# Hangman pictures for UI
HANGMAN_PICTURES = ['''
    +---+
    |   |
        |
        |
        |
        |
   =========''', '''
    +---+
    |   |
    o   |
        |
        |
        |
   =========''', '''
    +---+
    |   |
    o   |
    |   |
        |
        |
   =========''', '''
    +---+
    |   |
    o   |
   /|   |
        |
        |
   =========''', '''
    +---+
    |   |
    o   |
   /|\  |
        |
        |
   =========''', '''
    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
   ========''', '''
    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
   ========''']

WORDS = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks', 'coconut', 'enlightened',
         'snowstorm', 'python', 'solidity']

def check_letter_in_word(user_input):
    for index in range(0, len(chosen_word)):
        if chosen_word[index] == user_input:
            letters_guessed_right[index] = user_input
        else:
            continue


# Welcome prompt
print("Welcome to the game of Hangman, I wish you good luck")



lives_used = 0
letters_guessed_right = []
letters_guessed_wrong = []
chosen_word = random.choice(WORDS)
print(f"chosen word: {chosen_word}")

for line in range(len(chosen_word)):
    letters_guessed_right.append("_")

print("This is the word that you gotta guess:")

for i in letters_guessed_right:
    print(i, end=" ")
print("\n")

while lives_used < 6:
    print(HANGMAN_PICTURES[lives_used])
    guess = str(input("Guess a letter: ")).casefold()

    # Check if guessed letter is in the word
    if guess in letters_guessed_wrong:
        print("\nYou have already tried this letter!")
    elif guess in chosen_word:
        # Update the letters_guessed
        check_letter_in_word(guess)
        letters_guessed_wrong.append(guess)
        for i in letters_guessed_right:
            print(i, end=" ")
        print()

        # Check if player has guessed all the letters
        if "_" not in letters_guessed_right:
            print("\nCongratulations, you have guessed the word!")
            break
    else:
        print(f"Letter '{guess}' is not in the word!")
        letters_guessed_wrong.append(guess)
        lives_used += 1

if lives_used == 6:
    print(HANGMAN_PICTURES[6])
    print("GAME OVER")
    print(f"The word you were trying to guess was '{chosen_word}'.")
