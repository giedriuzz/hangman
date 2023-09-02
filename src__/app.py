"""Main game script"""

import logging
import logging.config
import sys
from random import choice

from hangman import hangman
from main import Categories, Letter, Words
from rules import rules
from termcolor import colored
from validation import input_only_en_letters, input_only_integer_value_not_bigger
from words.words import words

logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)
logger = logging.getLogger("sampleLogger")


greeting = colored(
    " === Welcome to Hangman game! ===", "red", "on_light_blue", attrs=["bold"]
)
print("\n", greeting)

while True:
    CHOOSING = int(
        input_only_integer_value_not_bigger(
            3,
            f'\n{colored("1. Start the game", "yellow", attrs=["bold"])}'
            f'\n{colored("2. Rules", "green", attrs=["bold"])}'
            f'\n{colored("3. Quit", "red", attrs=["bold"])}'
            f'\n{colored("Choose: ", "blue")}',
        )
    )
    # * Game area
    if CHOOSING == 1:
        categories = Categories(words)
        categories_dict = categories.get_categories_enumerated()
        print()
        category = input_only_integer_value_not_bigger(
            len(categories_dict), categories.print_categories(categories_dict)
        )

        _SAY_DONT_GUESSED = "You don`t guessed a letter :("
        _say_guessing_word = colored("Guessing word: ", "blue", attrs=["bold"])
        _say_you_hanged = f'\n{colored("HANGED :( ", "red", "on_red", attrs=["bold"])}'
        _say_choose_category = colored("Category: ", "green")

        LENGTH = 0
        while LENGTH < 10:
            LENGTH += 1
            # Get category value, guessing word, guessed word in list
            logging.debug("Round: %s/10", LENGTH)  # * Logging
            get_category_value = categories_dict[category]
            logger.debug("Category: %s", get_category_value)  # * Logging
            guessing_word = choice(words[get_category_value])
            logger.debug("Guessing word: %s", guessing_word)  # * Logging
            guessed_word_in_list = list(guessing_word)
            word_declaration = Words(word=guessing_word)
            # Create empty word list, reset all lists and variables after each round
            letter = Letter(word_declaration, "")
            letter.LETTERS_LIST.clear()
            letter.reload_letters_list()
            letter.MATCHED_LETTERS.clear()
            letter.NOT_MATCHED_LETTERS.clear()
            letter.empty_word_list.clear()
            # Print game area
            print(f'\n{colored("Round: ", "red")} {LENGTH}/10')
            print(_say_choose_category, get_category_value)
            print(_say_guessing_word, *["_" for _ in range(len(guessing_word))])

            while True:
                string_only_en_letters = input_only_en_letters(
                    colored("Guess a letter or all word: ", "yellow")
                )
                logger.debug(
                    "Letter in input() : %s", string_only_en_letters
                )  # * Logging
                letter = Letter(word_declaration, string_only_en_letters)
                letter.create_empty_word_list()
                if letter.inspect_letters() is False:
                    continue
                STRING = letter.inspect_letters()
                if len(string_only_en_letters) == 1:
                    # * When letter is in word
                    if letter.is_letter_in_word() is True and STRING is True:
                        print(_say_choose_category, get_category_value)
                        print(
                            colored("Guessing word: ", "blue"),
                            *letter.replace_guessed_letter(),
                        )
                        if letter.is_word_guessed() is True:
                            print(colored(" == You guessed the word !!! == ", "yellow"))
                            logger.debug("Guessed word: %s", guessing_word)  # * Logging
                            logger.debug("Win a GAME!")  # * Logging
                            break
                        print(
                            colored("Letters left: ", "green"),
                            *letter.remove_used_letter_from_list(),
                        )
                        logger.debug(
                            "Guessed letter: %s", string_only_en_letters
                        )  # * Logging
                        continue
                    # * When letter is not in word
                    if letter.get_hangman() == 7:
                        print(_say_you_hanged)
                        print(colored(hangman[letter.get_hangman()], "red"))
                        print(
                            colored("Word was: ", "blue", attrs=["bold"]),
                            *guessed_word_in_list,
                        )
                        logger.debug("Lose a GAME!")  # * Logging
                        break
                    print(colored(_SAY_DONT_GUESSED, "red"))
                    print(hangman[letter.get_hangman()])
                    print(_say_choose_category, get_category_value)
                    print(
                        colored("Guessing word: ", "blue"),
                        *letter.replace_guessed_letter(),
                    )
                    print(
                        colored("Letters left: ", "green"),
                        *letter.remove_used_letter_from_list(),
                    )
                    logger.debug(
                        "Not guessed letter was: %s", string_only_en_letters
                    )  # * Logging
                    continue
                # * When word is not guessed
                if letter.is_word_equal(string_only_en_letters) is False:
                    print(_say_you_hanged)
                    print(colored(hangman[7], "red"))
                    print(
                        colored("Word was: ", "blue", attrs=["bold"]),
                        *guessed_word_in_list,
                    )
                    logger.debug(
                        "Not guesses word in input(): %s", string_only_en_letters
                    )  # * Logging
                    logger.debug("Lose a GAME!")  # * Logging
                    break
                logger.debug("Win a GAME!")  # * Logging
                print(colored(" == You guessed the word !!! == ", "yellow"))
                break
        logger.debug("GAME OVER!")  # * Logging
        print(colored(" == Game over == ", "red", attrs=["reverse", "blink"]))
    # * Rules area
    elif CHOOSING == 2:
        rules()
    # * Quit area
    elif CHOOSING == 3:
        print(
            f'{colored("Closed game application!", "red")}\n'
            f"If you want to play again, run "
            f'{colored("app.py", "red",attrs=["bold"])} file!'
        )

        sys.exit(0)
