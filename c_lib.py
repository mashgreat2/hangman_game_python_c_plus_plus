from ctypes import cdll
import ctypes
c_lib = cdll.LoadLibrary('./_c_lib.so')
# set the types of the functions in here or you can do it later when
# calling the c++ functions.
c_lib.greet_player_c.argtype = ctypes.c_char_p
c_lib.greet_player_c.restype = ctypes.c_char_p
c_lib.check_letter_in_word.argtype = [ctypes.c_char_p, ctypes.c_char_p]
c_lib.check_letter_in_word.restype = ctypes.c_int
c_lib.update_guessed_correctly.argtype = ctypes.c_int
c_lib.update_guessed_correctly.restype = ctypes.c_int
c_lib.generate_guessed_index_array.argtype = ctypes.c_int
c_lib.generate_guessed_index_array.restype = ctypes.POINTER(ctypes.c_int)

c_lib.generate_word.restype = ctypes.c_char_p
c_lib.build_display_text.argtypes = [
    ctypes.POINTER(ctypes.c_int32),
    ctypes.c_char_p,
    ctypes.c_int
]
c_lib.build_display_text.restype = ctypes.c_char_p
c_lib.update_guessed_index_array.argtypes = [
    ctypes.POINTER(ctypes.c_int32),
    ctypes.c_char,
    ctypes.c_char_p
]
c_lib.update_guessed_index_array.restype = ctypes.POINTER(ctypes.c_int)


# C++ greet player function
def ctypes_greet_player(name):
    # need to use encode and decode with utf-8 option or else
    # it does not work.
    _msg = c_lib.greet_player_c(name.encode('utf-8'))

    return _msg.decode('utf-8')

def ctypes_check_letter_in_word(str, letter):
    return c_lib.check_letter_in_word(str.encode('utf-8'), letter.encode('utf-8'))

def ctypes_update_guessed_correctly(n, b):
    return c_lib.update_guessed_correctly(n, b)

def ctypes_build_display_text(guessed_index_array, str, size):
    # my_list = [0,1,1,1,0,0,0,0]
    # my_list = [1,0,0,0,1,0,0,0,0,0]
    my_list_p = (ctypes.c_int32 * size)(*guessed_index_array)
    # my_string = "elephant"
    # my_string = "prosperous"
    result = c_lib.build_display_text(my_list_p, str.encode('utf-8'), size)
    return result.decode('utf-8')

# def py_int_generate_guessed_index_array(size):
#
#     return c_lib.generate_guessed_index_array(ctypes.c_int(size))
def py_int_generate_guessed_index_array(size):
    converted_arr=[]
    actual_arr = c_lib.generate_guessed_index_array(ctypes.c_int(size))
    for i in range(size):
        converted_arr.append(actual_arr[i])
    return converted_arr

def ctypes_update_guessed_index_array(my_list, char, word):
    my_list_p = (ctypes.c_int32 * len(my_list))(*my_list)
    new_list_p = c_lib.update_guessed_index_array(my_list_p, char.encode('utf-8'), word.encode('utf-8'))
    updated_list = [ new_list_p[x] for x in range( len( my_list ) ) ]
    return updated_list


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

def ctypes_generate_word():
    return c_lib.generate_word().decode('utf-8')


if __name__ == '__main__':
    # print( "Calling c++ add_two function in python. Adding 3+8:", ctypes_add_two(3,8) )
    # print()
    # print(ctypes_generate_word())
    pass

