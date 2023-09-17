"""Module for database connection and data manipulation"""

from datetime import datetime
from typing import List, Union

from database_r.db_r.db_base import Base
from database_r.models_r.game import Game
from database_r.models_r.user import User
from database_r.models_r.words import Words
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from words.words import words_list


class SqlDatabase:
    """Class for database connection and data manipulation"""

    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.engine = create_engine(f"sqlite:///{self.db_name}.db")

        session = sessionmaker(bind=self.engine)
        self.session = session()

    def create_database(self) -> None:  # [x] naudojama
        """Creates database if it does not exist"""
        Base.metadata.create_all(self.engine, checkfirst=True)

    def add_user_to_db(
        self, name: str, surname: str, email: str, passwd: str
    ) -> None:  # [ ] nenaudojama
        """_summary_

        Args:
            name (str): _description_
            surname (str): _description_
            email (str): _description_
            passwd (str): _description_
        """ """"""

        user = User(
            name=name,
            surname=surname,
            email=email,
            passwd=passwd,
        )

        self.session.add(user)
        self.session.commit()

    def add_game_to_db(
        self,
        game_id: str,
        word: str,
        guess_time: datetime,
        hanged: bool,
        guesses_made: int,
        user_id: int,
    ) -> None:  # [ ] nenaudojama
        """Add each game to database
        Args:
            game_id (str): _description_
            word (str): _description_
            guess_time (datetime): calculated by game
            hanged (bool): _description_
            guesses_made (int): _description_
            user_id (int): _description_
        """
        game = Game(
            game_id=game_id,
            word=word,
            guess_time=guess_time,
            hanged=hanged,
            guesses_made=guesses_made,
            user_id=user_id,
        )
        self.session.add(game)
        self.session.commit()

    def read_user_by_email(
        self, user_email: str
    ) -> Union[User, bool]:  # [ ] nenaudojama
        """
        Args:
            user_email (str): _description_
        Get user from base.
        function check is user email is unique
        """
        try:
            user = self.session.query(User).filter_by(email=user_email).one()
            if user:
                return user
            return False
        except NoResultFound:
            return False

    def user_games_by_user_id(
        self, user_id: int
    ) -> Union[Game, bool]:  # [ ] nenaudojama
        """
        Args:
            user_id (int): user id number
        Get games by user id from base.
        """
        try:
            games = self.session.query(Game).filter_by(user_id=user_id).all()
            games_id: list = []
            for game in games:
                games_id.append(game.game_id)
            return games_id
        except NoResultFound:
            return False

    def get_game_by_game_id(self, game_id: int) -> Union[Game, bool]:  # [ ] nenaudojama
        """
        Args:
            game_id (int): game id number
        Get game by game id from base.
        """
        try:
            game = self.session.query(Game).filter_by(game_id=game_id).all()
            return game
        except NoResultFound:
            return False

    def get_game_info_by_game_id(
        self, game_id: int
    ) -> Union[list, bool]:  # [ ] nenaudojama
        """
        Args:
            game_id (int): game id number
        Get game by game id from base.
        """
        try:
            game_date = (
                self.session.query(Game.gamed_time).filter_by(game_id=game_id).first()
            )

            game_time = (
                self.session.query(Game.guess_time).filter_by(game_id=game_id).all()
            )
            game_time = [i[0] for i in game_time]
            games_played = (
                self.session.query(Game.hanged).filter(Game.game_id == game_id).count()
            )
            games_wins = (
                self.session.query(Game.hanged)
                .filter(Game.game_id == game_id)
                .filter(Game.hanged == 1)
                .count()
            )
            games_lost = games_played - games_wins
            return [game_date, sum(game_time), games_wins, games_lost]
        except NoResultFound:
            return False

    def get_words_by_category_and_difficulty(
        self, set_category: str, difficulty: list
    ) -> List[str]:  # [ ] nenaudojama
        """
        Args:
            category (str): _description_
            difficulty (list): _description_
        Get words by category and difficulty from base.
        """
        starts: int = difficulty[0]
        ends: int = difficulty[1]
        words_by_category = []
        my_filter = self.session.query(Words).filter_by(category=set_category).all()

        for word in my_filter:
            if starts <= int(word.difficulty) <= ends:
                words_by_category.append(word.word)
        return words_by_category

    def get_words_by_category(self, category: str) -> list:  # [ ] nenaudojama
        """
        Args:
            category (str): _description_
        Get words by category from base.
        """
        words = self.session.query(Words).filter_by(category=category).all()
        words_list: list = []
        for word in words:
            words_list.append(word.word)
        return words_list

    def get_words_category(self) -> set:  # [ ] nenaudojama
        """
        Get unique words category from base.
        """
        words = self.session.query(Words).distinct().all()
        categories_list: list = []
        for word in words:
            categories_list.append(word.category)
        return set(categories_list)

    def get_values_from_table_words(self) -> list:  # [ ] nenaudojama
        """
        Get words from base.
        """
        words = self.session.query(Words).all()
        words_list: list = []
        for word in words:
            words_list.append(word.word)
        return words_list

    def check_if_word_in_base(
        self, category: str, word: str
    ) -> Union[str, bool]:  # [x] naudojama
        """
        Args:
            word (str): _description_
        Check if word in base.
        """
        try:
            words = (
                self.session.query(Words)
                .filter_by(category=category)
                .filter_by(word=word.upper())
                .one()
            )
            if not words:
                return True
            return False
        except NoResultFound:
            return False

    def load_data(self, word_for_db: list) -> None:  # [x] naudojama
        """Function for load words in database"""
        self.create_database()
        for list_item in word_for_db:
            for category, word_list in list_item.items():
                for word in set(word_list):
                    check_words = self.check_if_word_in_base(category, word)
                    if check_words is False:
                        word_difficulty = len(word)
                        add_word = Words(
                            word=word.upper(),
                            category=category.upper(),
                            difficulty=word_difficulty,
                        )
                        self.session.add(add_word)
                        try:
                            self.session.commit()
                        except IntegrityError:
                            self.session.rollback()
                    continue


if __name__ == "__main__":
    db = SqlDatabase("hangman")
    db.load_data(words_list)
    # print(db.read_user_by_email("giedrius@g.lt").email)
