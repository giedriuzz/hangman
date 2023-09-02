"""Module for work with guessing word from database"""

from dataclasses import dataclass
from random import choice
from typing import Dict, List, Union

from termcolor import colored

# pylint: disable=line-too-long


@dataclass
class Words:
    """Word class"""

    word: str


class Letter:
    """Class for work with letters and words"""

    LETTERS_LIST_TUPLE = (
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    )

    MATCHED_LETTERS: List[str] = []
    NOT_MATCHED_LETTERS: List[str] = []
    LETTERS_LIST: List[str] = []
    empty_word_list: List[str] = []

    def __init__(self, word: Words, letter: str = ""):
        self.word = word.word
        self.letter = letter

    def create_empty_word_list(self) -> None:
        """Create empty word list"""
        if len(self.empty_word_list) == 0:
            for _ in range(len(self.word)):
                self.empty_word_list.append("_")

    def reload_letters_list(self) -> None:
        """Reload list of letters"""
        for letter in self.LETTERS_LIST_TUPLE:
            self.LETTERS_LIST.append(letter)

    def inspect_letters(self) -> bool:
        """Inspect is not used letters before"""

        if (
            self.letter not in self.MATCHED_LETTERS
            and self.letter not in self.NOT_MATCHED_LETTERS
        ):
            return True
        print("You have already used this letter!")
        return False

    def is_letter_in_word(self) -> Union[bool, str]:
        """Check if a letter is in the word"""
        if self.letter in self.word:
            self.MATCHED_LETTERS.append(self.letter)
            return True
        if self.letter not in self.word:
            self.NOT_MATCHED_LETTERS.append(self.letter)
            return False
        return self.letter

    def replace_guessed_letter(self) -> list:
        """Replace a letter if it is in the word"""
        for get_letter in enumerate(self.word):
            if get_letter[1] == self.letter.upper():
                self.empty_word_list[get_letter[0]] = self.letter.upper()
            continue
        return self.empty_word_list

    def remove_used_letter_from_list(self) -> List[str]:
        """Remove used letter from list"""
        self.LETTERS_LIST.remove(self.letter.upper())
        return self.LETTERS_LIST

    def get_hangman(self) -> int:
        """Return hangman picture"""
        return self.NOT_MATCHED_LETTERS.index(self.letter.upper())

    def is_word_guessed(self) -> bool:
        """Return guessed word for write to db"""
        alpha = "".join(self.empty_word_list)
        if alpha.isalpha() is True:
            return True
        return False

    def is_word_equal(self, word: str) -> bool:
        """Check if a word is equal to a guess"""
        if self.word == word.upper():
            return True
        return False

    def get_guesses(self) -> int:
        """Get guesses"""
        return len(Letter.NOT_MATCHED_LETTERS) + len(Letter.MATCHED_LETTERS)


class Categories:  # ! Vienaskaita
    """Class for work with categories"""

    def __init__(self, input_list: list):
        self.input_list = input_list

    def get_categories_enumerated(self) -> Dict[int, str]:
        """Get categories enumerated"""
        categories_dict = {}
        for category in enumerate(self.input_list, 1):
            categories_dict.update({category[0]: category[1].capitalize()})
        return categories_dict

    def print_categories(self, categories_dict: dict) -> str:
        """Print categories"""
        colors = [
            "red",
            "green",
            "yellow",
            "blue",
            "magenta",
            "cyan",
            "white",
            "light_red",
            "light_green",
            "light_yellow",
            "light_blue",
            "light_magenta",
            "light_cyan",
        ]
        print(
            f'{colored("           Categories               ","black", "on_white", attrs=["bold"])}\n'  # noqa: E501
        )
        for category_key, category_value in categories_dict.items():
            random_color = choice(colors)
            print(
                f"        {colored(category_key, random_color, attrs=['bold'])}."
                f"{colored(category_value, random_color, attrs=['bold'])}"
            )
        return colored("\nChoose a category: ", "blue")


if __name__ == "__main__":
    pass
