"""Module for database data manipulation"""

import time
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import Union

from db_direct import SqlDatabase
from termcolor import colored


# pylint: disable=line-too-long consider-using-f-string
class Abstract(ABC):
    """Blueprint for database data manipulation"""

    @abstractmethod
    def check_user_by_passwd_mail(self, user_passwd: str, user_email: str):
        """Check if user exists in database"""

    def get_games_by_user_id(self, user_id: int) -> list:
        """Get games by user id"""


class DatabaseIntermediate(Abstract):
    """Class for database data manipulation"""

    def __init__(self, db_name: str) -> None:
        self.base = SqlDatabase(db_name)

    def check_user_by_passwd_mail(
        self, user_passwd: str, user_email: str
    ) -> Union[tuple, bool]:
        """Check if user exists in database"""
        user = self.base.get_user_by_email(user_email=user_email)
        if user and user_passwd == user.passwd:
            return user.name, user.id
        return False

    def get_unique_games_id_by_user_id(self, user_id: int) -> list:
        """Get games by user id"""
        games = self.base.user_games_by_user_id(user_id=user_id)
        return list(set(games))

    def get_user_for_register(
        self, name: str, surname: str, email: str, passwd: str
    ) -> None:
        """Get user credentials for register"""
        self.base.add_user_to_db(
            name=name,
            surname=surname,
            email=email,
            passwd=passwd,
        )

    def get_words_by_category_difficulty(self, category: str, difficulty: int) -> list:
        """Get words by category and difficulty"""
        category = category.lower()
        if difficulty == 1:
            difficulty = (1, 4)
        if difficulty == 2:
            difficulty = (5, 8)
        if difficulty == 3:
            difficulty = (9, 12)
        words = self.base.get_words_by_category_and_difficulty(
            set_category=category, difficulty=(difficulty[0], difficulty[1])
        )
        return words

    def get_category(self) -> list:
        """Get category"""
        category = self.base.get_words_category()
        return [*category]

    def add_round(
        self,
        game_id: int,
        word: str,
        guess_time: datetime,
        hanged: bool,
        guesses_made: int,
        user_id: int,
    ) -> None:
        """Add round"""
        self.base.add_game_to_db(
            game_id=game_id,
            word=word,
            guess_time=guess_time,
            hanged=hanged,
            guesses_made=guesses_made,
            user_id=user_id,
        )

    def get_game_info(self, game_id: int) -> None:
        """Get game info"""
        game = self.base.get_game_info_by_game_id(game_id=game_id)

        text = (
            f"\n{colored('Game info...', 'blue')}"
            f"\n\nGame date: {colored(game[0][0].date(), 'blue')}"
            f'\nGame time: {colored("{}".format(str(timedelta(seconds=game[1]))), "blue")}'  # noqa: E501
            f"\nGames wined: {colored(game[2], 'blue')}"
            f"\nGames lost: {colored(game[3], 'blue')}\n"
        )
        time.sleep(1)
        print(text)

    def get_rounds_info(self, game_id: int) -> None:
        """Get rounds info"""
        rounds = self.base.get_game_by_game_id(game_id=game_id)
        round_number = 0

        for one_round in rounds:
            round_number += 1
            if round_number <= 9:
                rounds_number = " " + str(round_number) + "."
            else:
                rounds_number = str(round_number) + "."
            if one_round.hanged == 0:
                hanged = "Yes"
            else:
                hanged = "No"
            text = (
                f"{rounds_number} Guessed word: {colored(one_round.word, 'blue')}"
                f" | Guesses made: {colored(one_round.guesses_made, 'blue')}"
                f" | Guess time: {colored('{}'.format(str(timedelta(seconds=one_round.guess_time))), 'blue')}"  # noqa: E501
                f" | Hanged: {colored(hanged, 'blue')}"
            )
            time.sleep(0.1)
            print(text)


if __name__ == "__main__":
    ...
