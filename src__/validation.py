"""Module for validating inputs"""
import datetime
import random
import time


def input_only_integer_value_not_bigger(value_size: int, input_text: str) -> int:
    """Validate input is integer not bigger than value size
    value_size: max value size
    input_text: what text want to see in input line"""
    while True:
        string = input(input_text)
        if string.isdigit() is True and int(string) <= value_size:
            return int(string)
        print(f"Input must to be an integer value not bigger than: {value_size} !")


def return_dict_value_by_key(value_size: int, input_text: str, word_dict: dict) -> str:
    """Validate input is integer not bigger than value size
    value_size: max value size
    input_text: what text want to see in input line
    word_dict: dictionary with values"""
    while True:
        string = input(input_text)
        if string.isdigit() is True and int(string) <= value_size:
            return word_dict.get(int(string))
        print(f"Input must to be an integer value not bigger than: {value_size} !")


def input_only_en_letters(input_text: str) -> str:
    """Validate input is it only letters from English alphabet
    input_text: what text want to see in input line"""
    lt_letters_list = ["Ą", "Č", "Ę", "Ė", "Į", "Š", "Ų", "Ū", "Ž"]
    while True:
        string = input(input_text).upper()
        if string.isalpha() is True:
            filtered = filter(lambda letter: letter in string, lt_letters_list)
            if len(list(filtered)) == 0:
                return string
            print("Input accepts only English alphabetic letters!")
            continue
        print("Input accepts only English alphabetic letters!")
        continue  # check if need


def input_only_email(email: str) -> str:
    """Validate input is it only email"""
    while True:
        string = input(email)
        if string.find("@") != -1:
            return string
        print("Input accepts only email!")
        continue


def input_only_letters(input_text: str) -> str:
    """Validate input is it only letters
    input_text: what text want to see in input line"""
    while True:
        string = input(input_text)
        if string.isalpha() is True:
            return string
        print("Input accepts only letters!")
        continue


def get_unique_id() -> int:
    """Get unique id"""
    timestamp = int(time.time())
    random_number = random.randint(1000, 9999)
    return timestamp - random_number


def get_gaming_time(start_time: datetime, end_time: datetime) -> datetime:
    """Get gaming time"""
    gaming_time = start_time - end_time
    return int(gaming_time.total_seconds())
