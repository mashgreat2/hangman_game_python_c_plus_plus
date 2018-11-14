from ctypes import cdll
import ctypes
c_lib = cdll.LoadLibrary('./_c_lib.so')

# This is a Python function that calls a C++ add_two function
def ctypes_add_two(x, y):
    return c_lib.add_two_c(ctypes.c_int(x), ctypes.c_int(y))

# Call the Fibonacci function in C++
def ctypes_fib_num(n):
    return c_lib.fib_num_c(ctypes.c_int(n))

# Define the Fibonacci function in Python
def py_fib_num(n):
    if ( n <= 1 ): return n
    return py_fib_num(n-2) + py_fib_num(n-1)

if __name__ == '__main__':
    print( "Calling c++ add_two function in python. Adding 3+8:", ctypes_add_two(3,8) )