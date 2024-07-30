
# Hangman Game

Welcome to the classic Hangman game implemented in Python. This program allows you to play Hangman with a variety of words, providing an engaging and interactive experience.

## Features

- **Random Word Selection**: The game randomly selects a word from a predefined list of words.
- **Visual Feedback**: The game displays hangman pictures to indicate the player's progress.
- **Input Validation**: The game checks for valid inputs, ensuring the player enters a single letter.
- **User-Friendly Interface**: The game provides clear instructions and feedback on each guess.

## Requirements

- Python 3.x

## How to Play

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/0x2V369/hangman.git
    cd hangman-game
    ```

2. **Run the Game:**
    ```sh
    python hangman.py
    ```

3. **Follow the Instructions:**
    - The game will display the hangman board and the word to guess as underscores.
    - Enter a single letter as your guess.
    - The game will indicate if the letter is in the word and update the display accordingly.
    - You have up to 6 incorrect guesses before the game is over.

## Example

```sh
Welcome to the game of Hangman, I wish you good luck
This is the word that you gotta guess:
_ _ _ _ _ _ _ 

Guess a letter: e
Letter 'e' is not in the word!

+---+
|   |
o   |
    |
    |
    |
=========

Current progress: _ _ _ _ _ _ _ 

...

Congratulations, you have guessed the word!
```

## Code Overview

The code consists of the following key functions:

- `choose_word(words)`: Selects a random word from the list.
- `display_current_progress(letters_guessed_right)`: Displays the current state of the guessed word.
- `check_letter_in_word(chosen_word, user_input, letters_guessed_right)`: Updates the guessed letters if the user's guess is correct.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

This Hangman game was developed by [0x2V369](https://github.com/0x2V369).
