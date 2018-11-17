cmake_minimum_required(VERSION 3.12)
project(hangman_python)

set(CMAKE_CXX_STANDARD 11)

add_executable(hangman_python _c_lib.cc)