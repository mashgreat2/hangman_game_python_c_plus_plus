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
using namespace std;

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

#include "random_words.dat"
#include <random>


//randomly selects word for user to guess throughout game
extern "C" char const* generate_word() {
  size_t min = 0;
  int max = 7938;
  std::random_device rd;
  std::mt19937 rng(rd());
  std::uniform_int_distribution<int> uni(min,max);

  size_t rindex = uni(rng);

  char const *word = words_list[rindex];
  return word;

}

extern "C" int * generate_guessed_index_array(int size){
  int *array = new int [size];
  for (int i = 0; i<size;i++) {
    array[i] = 0;
  }

  return array;
}

// Check if the user has guessed at least one letter correctly.
extern "C" int check_letter_in_word(char * str, char * letter) {
  int correct = 0;
  for (int i = 0; i < strlen(str); i++) {
    if (str[i] == letter[0])
      correct++;
  }
  if (correct > 0)
    return 1;
  return 0;
}

extern "C" int * update_guessed_index_array(int * arr, char c, char * str){
  size_t length = strlen(str);
  int *updated_array = new int [length];
  for( int i=0; i<length; i++ ){
    if ( str[i] == c ){ updated_array[i] = 1; }
    else { updated_array[i] = arr[i]; }
  }
  return updated_array;
}

// Create a greeting message with a given player name.
extern "C" char * greet_player_c(char str[]) {
  char greeting[] = "Hello, ";
  char message[] = ". Get ready to play some hangman!";
  size_t len = 0;
  len = strlen(str) + strlen(greeting) + strlen(message);
  char * final = new char[len];
  strcat(final, greeting);
  strcat(final, str);
  strcat(final, message);
  return final;
}


// update guessed correctly variable. return n + 1 if b is 1
extern "C" int update_guessed_correctly(int n, int b) {
  if (b == 1) { return n + 1; }
  return n;
}

extern "C" char * build_display_text(int * guessed_index_array, char * str, int size) {
  char * final = new char[size+1];
  for (int i = 0; i < size; i++) {
    if ( guessed_index_array[i] == 1 ) { final[i] = (char) str[i]; }
    else { final[i] = '.'; }
  }
  final[size] = '\0'; // need the null terminator..otherwise it doesnt work. spent 1 hour on this bug..
  return final;
}

//extern "C" void free_string(char* str) {
//  delete str;
//}

int main() {
//  std::cout << "Hello world!" << "\n";
//    std::cout << "adding 7+8: " << add_two(7,8) << "\n";
//  int k = 5;
//  std::cout << "k before: " << k << "\n";
//  k = update_guessed_correctly(5, 1);
//  std::cout << "k after: " << k << "\n";
//  int arr[] = {0,1,0,1,0,0,0,0};
//  char word[] = "elephant";
//  build_display_text(arr, word, 8);
//  cout << "arr: ";
//  for (int i = 0; i < 8; ++i) {
//    cout << arr[i] << ", ";
//  }
//  cout << endl;
//  update_guessed_index_array(arr, 'e', word);
//  cout << "arr(after update): ";
//  for (int i = 0; i < 8; ++i) {
//    cout << arr[i] << ", ";
//  }
//  cout << endl;
//  char const *newWord = generate_word();
//  std::cout << newWord << std::endl;
//  std::cout << newWord[1] << std::endl;
  return 0;
}
