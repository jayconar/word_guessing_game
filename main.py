import random
from data import data


def choose_random_word(word_list):
    return random.choice(word_list).lower()


def display_word(word, guessed_letters):
    display = [letter if letter in guessed_letters else '_' for letter in word]
    return ' '.join(display)


def load_word_list():
    try:
        with open("vocabulary.txt", "r") as file:
            word_list = [line.strip() for line in file]
    except (FileNotFoundError, IOError):
        print("Creating the word bank..")
        data()
        with open("vocabulary.txt", "r") as file:
            word_list = [line.strip() for line in file]

    return word_list


def main():
    word_list = load_word_list()

    chosen_word = choose_random_word(word_list)
    guessed_letters = set()
    life = 6

    print("\nWelcome to the Word Guessing Game!")
    print(display_word(chosen_word, guessed_letters))

    fin = False
    while not fin:
        guess = input('\nGuess a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in chosen_word:
            print("Good guess, keep going!")
        else:
            life -= 1
            if life > 0:
                print("You lost a life. Lives left:", life)
            else:
                print("Game Over. You've lost all of your lives.\nThe word was: ", chosen_word)
                fin = True
        current_display = display_word(chosen_word, guessed_letters)
        if '_' not in current_display:
            print(f"{current_display}\nWell done! You win!")
            fin = True
        if not fin:
            print(current_display)
        elif fin:
            if input("Do you want to play again (y/n): ") == 'y':
                main()


main()
