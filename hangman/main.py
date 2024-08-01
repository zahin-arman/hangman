import random
from words import words
import string


def get_valid_words(words_list):
    word = random.choice(words_list)
    while '-' in word or ' ' in word:
        word = random.choice(words_list)
    return word.upper()


def hangman():
    word = get_valid_words(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    lives = len(word) + 2

    # getting_user_input
    while len(word_letters) > 0 and lives > 0:

        # used letters
        print(f"Lives: {lives}")
        print(f"You have already used these letters: {' '.join(used_letters)}")

        # What current word is
        current_guessed_state = [letter if letter in used_letters else '-' for letter in word]
        print(f"Current guessed state: {' '.join(current_guessed_state)}")

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabets and user_letter not in used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
        elif user_letter in used_letters:
            print(f"You have already used '{user_letter}'.Please try again. \n")
        else:
            print(f"Invalid character. Please try again. \n")

    if lives == 0:
        print(f"You have died. The word was {word}")
    else:
        print("You have won! You had", lives, "live(s) left.")
        print(f"The word was {word}")


hangman()
