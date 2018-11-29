# hangman_game_python_c_plus_plus

![](hangman_screenshot.png)

In this project, we implement a simple Hangman game that you can play with the Python console. 

The purpose of this project is to learn how to integrate C++ with Python.

Game business logic will be calculated by using C++ functions, and Python will 
be mostly used to start, and end the game, and to print out information to the user about the state 
of the game.

How to play:

You can clone the repository and type in terminal: "python ./main.py" to start 
the game. 

The C++ functions that called are written in the file '_c_lib.cc' and the 
corresponding compatible functions are written in the file 'c_lib.py'. Our main.py 
game file calls the functions from the 'c_lib.py' Python file.