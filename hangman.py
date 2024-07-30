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


def choose_word(words):
    return random.choice(words)


def display_current_progress(letter_guessed_right):
    print("Current progress : ", " ".join(letters_guessed_right))
    print("\n")


def check_letter_in_word(chosen_word, user_input, letters_guessed_right):
    for index in range(len(chosen_word)):
        if chosen_word[index] == user_input:
            letters_guessed_right[index] = user_input


print("Welcome to the game of Hangman, I wish you good luck")

lives_used = 0
chosen_word = choose_word(WORDS)
letters_guessed_right = ["_" for _ in range(len(chosen_word))]
letters_guessed_wrong = []

print("This is the word that you gotta guess:")
display_current_progress(letters_guessed_right)

while lives_used < 6:
    print(HANGMAN_PICTURES[lives_used])
    display_current_progress(letters_guessed_right)
    guess = str(input("Guess a letter: ")).casefold()

    if len(guess) != 1 or not guess.isalpha():
        print("\nPlease enter single letter!")
        continue

    if guess in letters_guessed_wrong or guess in letters_guessed_right:
        print(f"\nYou have already tried '{guess}'!")
        continue

    if guess in chosen_word:
        check_letter_in_word(chosen_word, guess, letters_guessed_right)
    else:
        print(f"Letter '{guess}' is not in the word!")
        letters_guessed_wrong.append(guess)
        lives_used += 1

    if "_" not in letters_guessed_right:
        display_current_progress(letters_guessed_right)
        print("\nCongratulations, you have guessed the word!")
        break

if lives_used == 6:
    print(HANGMAN_PICTURES[6])
    print("GAME OVER")
    print(f"The word you were trying to guess was '{chosen_word}'.")
