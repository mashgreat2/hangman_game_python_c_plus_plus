from ctypes import cdll
import ctypes
c_lib = cdll.LoadLibrary('./_c_lib.so')

# This is a python function that calls a C++ function

def ctypes_add_two(x, y):
    return c_lib.add_two_c(ctypes.c_int(x), ctypes.c_int(y))



if __name__ == '__main__':
    print( "Calling c++ add_two function in python. Adding 3+8:", ctypes_add_two(3,8) )