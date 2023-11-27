# Word Guessing Game
Simple command line python program with a large list of words

### Run only the main.py file. 
Run it only after the installation of the required packages specified in requirements.txt.

### data.py
Creates an enormous collection of 4-to-8 letter-long words with not more than 4 syllables, and stores it in a text file.
Called from the main file only if the text file is missing or not created yet.

### Game Rules:
Player has six lives.
A random word with underscores replacing each letter is displayed on the screen. Making the word length obvious.
Player has to guess a letter that might be in the word.
If the guessed letter is in the word, the position(s) of the letter in the word is revealed.
Games goes on till the player looses all lives by making wrong guesses or guesses all the letters before losing all six lives.
Input 'y' after that to play again.
