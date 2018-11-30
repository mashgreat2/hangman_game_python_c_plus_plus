# CS 2024 Final Assignment, Python file.
# Created by
# SM Mashuque ( sm2344 ),
# Vy Nguyen ( vqn2 ),
# Anna Shats ( as2639 )
# Chris Schwarze ( cs977 )
#
# on 11/11/2018

import c_lib

def run_hangman():
    name = input("What is your name?\n")

    welcome_message = c_lib.ctypes_greet_player(name)
    print(welcome_message)

    guesses_allowed = 7

    picked_word = c_lib.ctypes_generate_word()
    #print(picked_word)

    N = len(picked_word)


    #trying to call words using the c++ func indexed array

    letters_guessed = c_lib.py_int_generate_guessed_index_array(N)


    guessed_correctly = 0

    lines = "." * N
    print("\n", lines)

    while ( guesses_allowed > 0 and guessed_correctly < N ):
        letter = input(
            "\nGuess a letter in this word of " +
            str(N) + " letters. You have: " +
            str(guesses_allowed) +
            " guesses left.\n"
        )
        while (letter == ""):
            letter = input(
                "\nInput can't be blank; enter a letter\n"
            )

        guessed_one_at_least = c_lib.ctypes_check_letter_in_word(picked_word, letter) == 1
        letters_guessed = c_lib.ctypes_update_guessed_index_array(letters_guessed, letter, picked_word)
        guessed_correctly = letters_guessed.count(1)

        if not guessed_one_at_least:
            guesses_allowed -= 1
            print(
                "No matches. Try again." +
                "You have: " + str(guesses_allowed) +
                " guesses left.\n"
            )

        lines = c_lib.ctypes_build_display_text(letters_guessed, picked_word, len(picked_word))

        print("\n", lines)

    # Todo: This can be a method in C++ that decides what final message to show the user.
    if guessed_correctly == N:
        print("Congratulations, you win!")
    else:
        print("Failed to guess correctly. Try again.")




if __name__ == '__main__':
    run_hangman()
