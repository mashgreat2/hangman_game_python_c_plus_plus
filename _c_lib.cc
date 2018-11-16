/*
 * CS 2024 Final Assignment, C++ library file.
 * Created by SM Mashuque ( sm2344 ),
 *
 *
 *
 *
 * on 11/13/2018
 *
 * This is what I have learned on how to compile and run
 * C++ functions in the Python.
 *
 * 1. First you have to compile the C++ file and create the object file.
 * 2. Second you have to create a shared library file.
 * 3. Now you can call that shared library inside any Python file.
 *
 * 1. g++ -c -fPIC _c_lib.cc -o _c_lib.o
 *    - this line compiles and creates the object file.
 * 2. g++ -shared _c_lib.o -o _c_lib.so
 *    - this creates the shared library object file.
 *
*/

#include <iostream>

// need to add - extern “C” before C++ functions to make them work like
// a normal C function, so that it can work with Python.
// this is needed for Python to work with C++
extern "C" int add_two_c(int x, int y) {
  return x + y;
}

extern "C" int fib_num_c(int n) {
  if ( n <= 1 ) { return n; }
  return fib_num_c(n-2) + fib_num_c(n-1);
}

// Check if the user has guessed at least one letter correctly.
extern "C" int check_letter_in_word(char * str, char * letter) {
    int correct = 0;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == letter)
            correct++;
    }
    if (correct > 0)
        return 1;
    return 0;
}

// Create a greeting message with a given player name.
extern "C" char * greet_player_c(char str[]) {
//  std::cout << "str: " << str << "\n";
  char greeting[] = "Hello, ";
  char message[] = ". Get ready to play some hangman!";
  int len = 0;
  len = strlen(str) + strlen(greeting) + strlen(message);
//  std::cout << "len: " << len << "\n";
  char * final = new char[len];
  strcat(final, greeting);
  strcat(final, str);
  strcat(final, message);
//  std::cout << "final: " << final << "\n";
  return final;
}

extern "C" void free_string(char* str) {
  delete str;
}

int main() {
//    std::cout << "Hello world!" << "\n";
//    std::cout << "adding 7+8: " << add_two(7,8) << "\n";
  return 0;
}