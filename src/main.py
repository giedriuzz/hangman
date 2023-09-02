"""Main game module"""

while True:
    # Register, Login, Play as guest
    # Game menu when user is logged in: Play, Score, Exit
    # Game menu when user is not logged in: Play, Exit
    word = "CAFFE"
    guessing_word = ["_" for _ in range(len(word))]

    attempt = 0
    while attempt < 10:
        attempt += 1
        # print(underscore_word)
        print(*guessing_word)
        guessing_letter = input("Guess a letter: ").upper()
        if guessing_letter in guessing_word:
            letter_index = guessing_word.index(guessing_letter)
            new = guessing_word.insert(letter_index, guessing_letter)
            print(new)
            print("You guessed!")
            attempt -= 1
            continue
