"""File for rules of game"""

from termcolor import colored


def rules() -> None:
    """Print rules of game"""
    print(colored("\nHow to play hangman", "green", attrs=["bold"]))
    print(
        colored(
            "Hangman is a simple word guessing game. Player try to figure out an unknown",
            "green",
        )
    )
    print(
        colored(
            "word by guessing letters. If too many letters which do not appear in the word",
            "green",
        )
    )

    print(colored("are guessed, the player is hanged (and loses\n", "green"))
    print(
        colored(
            "As letters in the word are guessed, choose and write letter in terminal.",
            "green",
        )
    )
    print(
        colored(
            "If a letter not in the word is guess, you will see picture of a person on the",
            "green",
        )
    )
    print(
        colored(
            "gallows–one part for each incorrect letter guess. Most frequently, the person",
            "green",
        )
    )
    print(
        colored(
            "is drawn in 7 parts (for 7 letter guesses) in the order: gallows, head, body,",
            "green",
        )
    )
    print(colored("left leg, right leg, left arm, right arm, rope.\n", "green"))
    print(colored("You can guess by letter or by all word.", "green"))
    print(colored("If you want to guess by all word, write it in terminal.\n", "green"))
    print(colored("But be careful! ", "yellow", attrs=["bold"]))
    print(colored("When you make mistake and enter more than one letter,", "yellow"))
    print(colored("it will be taken as a guess of the word!\n", "yellow"))
