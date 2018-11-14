# CS 2024 Final Assignment, Python file.
# Created by
# SM Mashuque ( sm2344 ),
#
#
#
#
# on 11/11/2018

# Todo: design a better interface ?
def run_hangman():
    # name = input("What is your name?\n")

    # print("\nHi, " + name + ".\nGet ready to play some hangman!")

    guesses_allowed = 7
    # Todo: Get lots of words and choose one randomly by using the random.choice method equal of C++.
    words = ["elephant"]
    picked_word = list( words[0] )

    N = len(picked_word)

    letters_guessed = [False] * N
    guessed_correctly = 0

    lines = " _ " * N
    print("\n", lines)

    while ( guesses_allowed > 0 and guessed_correctly < N ):
        letter = input(
            "\nGuess a letter in this word of " +
            str(N) + " letters. You have: " +
            str(guesses_allowed) +
            " guesses left.\n"
        )
        guessed_one_at_least = False
        # Check if the user has guessed at least one letter correctly.
        # Todo: this can be a method written in C++
        for i in range(N):
            if ( letter == picked_word[i] ):
                letters_guessed[i] = True
                guessed_correctly += 1
                guessed_one_at_least = True

        if not guessed_one_at_least:
            guesses_allowed -= 1
            print(
                "No matches. Try again." +
                "You have: " + str(guesses_allowed) +
                " guesses left.\n"
            )

        # Build up the underscores or letters line to display user.
        # Todo: this can be done with a C++ function.
        lines = ""
        for i in range(N):
            if ( letters_guessed[i] == True ):
                lines = lines + " " + picked_word[i] + " "
            else:
                lines = lines + " _ "

        print("\n", lines)

    # Todo: This can be a method in C++ that decides what final message to show the user.
    if guessed_correctly == N:
        print("Congratulations, you win!")
    else:
        print("Failed to guess correctly. Try again.")




if __name__ == '__main__':
    run_hangman()
