"""Module for store text where is used in program"""
import maskpass
from termcolor import colored
from validation import input_only_email


def login_register_text() -> str:
    """Text for registration"""
    text = (
        f"\n\n{colored('        1. Register', 'white', attrs=['bold'])}"
        f"\n{colored('        2. Login', 'white', attrs=['bold'])}"
        f"\n{colored('        3. Play without registration', 'white', attrs=['bold'])}"
        f"\n"
        f"\nChoose: "
    )
    return text


def level() -> str:
    """Text for level"""
    text = (
        f'\n{colored("           Level               ","black", "on_white", attrs=["bold"])}'  # noqa: E501
        f"\n\n{colored('        1. Easy', 'white', attrs=['bold'])}"
        f"\n{colored('        2. Medium', 'white', attrs=['bold'])}"
        f"\n{colored('        3. Hard', 'white', attrs=['bold'])}"
        f"\nChoose: "
    )
    return text


def game_menu() -> str:
    """Text for game menu"""
    text = (
        f'\n{colored("           Game menu               ","white", "on_white", attrs=["bold"])}'  # noqa: E501
        f'\n\n{colored("        1. Start the game", "white", attrs=["bold"])}'
        f'\n{colored("        2. Rules", "white", attrs=["bold"])}'
        f'\n{colored("        3. You Games", "white", attrs=["bold"])}'
        f'\n{colored("        4. Quit", "white", attrs=["bold"])}'
        f"\n\nChoose: "
    )
    return text


def game_menu_quest() -> str:
    """Text for game menu"""
    text = (
        f'\n{colored("           Game menu               ","white", "on_white", attrs=["bold"])}'  # noqa: E501
        f'\n\n{colored("        1. Start the game", "white", attrs=["bold"])}'
        f'\n{colored("        2. Rules", "white", attrs=["bold"])}'
        f'\n{colored("        3. Quit", "white", attrs=["bold"])}'
        f"\n\nChoose: "
    )
    return text


def input_email() -> str:
    """Text for input email"""
    email = input_only_email(colored("Email: ", "white"))
    return email
    # return text


def input_passwd() -> str:
    """Text for input password"""
    passwd = maskpass.askpass(prompt=colored("Password: ", "white"), mask="*")
    return passwd
