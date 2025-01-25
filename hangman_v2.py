"""
Hangman Game
This module contains a simple Hangman game implementation.
"""

from hangman_library import HANGMAN_WORD_LIST, HANGMANPICS, HANGMAN_TITLE
import random

MAX_GUESSES = 6


def get_word_for_game():
    """Returns a random word from HANGMAN_WORD_LIST"""
    return random.choice(HANGMAN_WORD_LIST)


def get_user_input(used_letters):
    """
    Get and validate user input
    :param used_letters:
    :return: valid user input as a single letter
    """
    while True:
        letter = input("Guess a letter: ").casefold().strip()

        if len(letter) != 1 or not letter.isalpha():
            print("You must enter a single letter!")
        elif letter in used_letters:
            print(f"Letter '{letter}' has already been guessed. Try again!")
        else:
            return letter


def check_user_input(hangman_word, word_to_guess, user_guess):
    """
    Updates the guessed word if the user's guess is correct.
    :param hangman_word: Current state of guessed letters.
    :param word_to_guess: The actual word to be guessed.
    :param user_guess: The letter guessed by the user.
    :return: Updated hangman_word and whether the guess was correct.
    """
    guess_correct = False

    for i, char in enumerate(word_to_guess):
        if user_guess == char:
            hangman_word[i] = user_guess
            guess_correct = True

    return hangman_word, guess_correct


def main():
    print(HANGMAN_TITLE)

    word_to_guess = get_word_for_game()
    hangman_word = ["_" for _ in word_to_guess]
    guessed_letters = []
    wrong_guesses = 0

    while wrong_guesses < MAX_GUESSES:
        print(f"Word to guess: {" ".join(hangman_word)}")
        print(HANGMANPICS[wrong_guesses])

        user_guess = get_user_input(guessed_letters)
        guessed_letters.append(user_guess)

        hangman_word, user_guess_correct = check_user_input(hangman_word, word_to_guess, user_guess)

        if not user_guess_correct:
            print(f"\nLetter '{user_guess}' is not in the word!")
            wrong_guesses += 1

        # Check win condition
        if "_" not in hangman_word:
            print(f"Congratulations, you won! The correct word was: {word_to_guess}")
            return

        # Print the lives left after each guess
        print(f"\n{'*' * 20}{6 - wrong_guesses}/{MAX_GUESSES} LIVES LEFT {'*' * 20}\n")

    # If the loop exits, the player lost
    print(HANGMANPICS[MAX_GUESSES])
    print(f"You lost! The correct word was: {word_to_guess}!")


if __name__ == '__main__':
    main()
