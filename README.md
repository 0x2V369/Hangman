# Hangman Game

Welcome to the classic Hangman game implemented in Python. This repository now contains **two** different versions of Hangman:

1. **Original Version**: `hangman.py`
2. **Enhanced Version**: `hangman_v2.py` (uses `hangman_library.py` for an expanded word list and ASCII art)

## Features

- **Random Word Selection**  
  - In `hangman.py`, the word list is defined within the same file.  
  - In `hangman_v2.py`, the word list is imported from `hangman_library.py` (`HANGMAN_WORD_LIST`), offering a much larger variety of possible words.

- **Visual Feedback**  
  - Both versions display hangman pictures to indicate your progress.  
  - The updated version (`hangman_v2.py`) uses ASCII art from `hangman_library.py` (`HANGMANPICS` and `HANGMAN_TITLE`).

- **Input Validation**  
  - Both versions ensure the user enters a single letter at a time, handling incorrect and repeated guesses.

- **Multiple Game Modes**  
  - You can choose to run either the original or the enhanced version, depending on what experience you want.

- **User-Friendly Interface**  
  - Clear instructions and feedback are provided in both versions.

## File Overview

Below is a brief description of each file in this repository:

- **`hangman.py`**  
  - The original Hangman game script with a shorter word list and its own ASCII art.

- **`hangman_library.py`**  
  - Contains the larger `HANGMAN_WORD_LIST`, ASCII art (`HANGMANPICS`) and a stylish title banner (`HANGMAN_TITLE`).  
  - Designed to be imported by other Hangman implementations, like `hangman_v2.py`.

- **`hangman_v2.py`**  
  - An enhanced Hangman implementation that imports words, ASCII art, and banner from `hangman_library.py`.  
  - Demonstrates a more modular design and a larger variety of words.

- **`README.md`**  
  - Provides documentation and instructions for running both versions of the game.

## Requirements

- Python 3.x

## How to Play

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/0x2V369/hangman.git
    cd hangman-game
    ```
2. **Choose Which Version to Run:**
    - **Original Version (`hangman.py`):**
      ```bash
      python hangman.py
      ```
    - **Enhanced Version (`hangman_v2.py`):**
      ```bash
      python hangman_v2.py
      ```
3. **Follow the On-Screen Instructions:**
    - A word will be randomly selected.
    - You have up to 6 incorrect guesses before the game ends.
    - Enter a single letter as your guess each time you are prompted.

## Example (Enhanced Version)

Below is a short example of how it looks when you run `hangman_v2.py`:

```text
 _                                             _ 
| |                                           | |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __ | |
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \| |
| | | | (_| | | | | (_| | | | | | | (_| | | | |_|
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_(_)
                    __/ |                        
                   |___/                         

Word to guess: _ _ _ _ _

  +---+
  |   |
      |
      |
      |
      |
=========

Guess a letter: e
```

If the letter is correct, the display is updated. If it’s incorrect, the hangman grows, and the number of lives decreases. Good luck!

## Code Highlights

### Original Version (`hangman.py`)
- **Functions**:
  - `choose_word(words)`: Chooses a random word from a small, built-in list.
  - `display_current_progress(letters_guessed_right)`: Prints out the current guess state.
  - `check_letter_in_word(chosen_word, user_input, letters_guessed_right)`: Checks and updates correct letters.

### Enhanced Version (`hangman_v2.py`)
- **Key Highlights**:
  - **Modular Design**: Imports `HANGMAN_WORD_LIST`, `HANGMANPICS`, and `HANGMAN_TITLE` from `hangman_library.py`.
  - **get_word_for_game()**: Chooses a word from the large external word list.
  - **get_user_input(used_letters)**: Validates input and checks if letters were already used.
  - **check_user_input()**: Updates correctly guessed letters in the word.

### Supporting Module (`hangman_library.py`)
- **`HANGMAN_WORD_LIST`**: Extensive list of possible words to guess.
- **`HANGMANPICS`**: A larger ASCII representation of the hangman for the enhanced version.
- **`HANGMAN_TITLE`**: ASCII art displayed at the start of `hangman_v2.py`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

This Hangman game was developed by [0x2V369](https://github.com/0x2V369).