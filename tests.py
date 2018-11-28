import unittest
import c_lib

class TestCandPythonFunctions(unittest.TestCase):

    def test_ctypes_add_two(self):
        self.assertEqual(c_lib.ctypes_add_two(5,9), 14)

    def test_ctypes_greet_player(self):
        actual_msg = c_lib.ctypes_greet_player("SM Mash")
        expected_msg = "Hello, " + "SM Mash" + ". Get ready to play some hangman!"
        self.assertEqual(actual_msg, expected_msg)

        actual_msg = c_lib.ctypes_greet_player("Jane Doe")
        expected_msg = "Hello, " + "Jane Doe" + ". Get ready to play some hangman!"
        self.assertEqual(actual_msg, expected_msg)
        print("test_ctypes_greet_player PASSED.")


    def test_generate_guessed_index_array(self):

        n = 5

        actual_msg = c_lib.py_int_generate_guessed_index_array(n)
        expected_msg = [0,0,0,0,0]
        self.assertEqual(actual_msg, expected_msg)
        print("test_generate_guessed_index_array PASSED.")

    def check_letter_in_word(self):

        str = "hello"
        letter = "l"

        actual_bool = c_lib.py_check_letter_in_word(str, letter)
        self.assertEqual(actual_bool, 1)

        print("test_check_letter_in_word PASSED.")

    def test_ctypes_update_guessed_index_array(self):
        arr = [0, 1, 0, 1, 0, 0, 0, 0]
        word = "elephant"
        char = 'e'
        actual_arr = c_lib.ctypes_update_guessed_index_array(arr, char, word)
        expected_arr = [1, 1, 1, 1, 0, 0, 0, 0]
        self.assertEqual(actual_arr, expected_arr)

        char = 't'
        actual_arr = c_lib.ctypes_update_guessed_index_array(expected_arr, char, word)
        expected_arr = [1, 1, 1, 1, 0, 0, 0, 1]
        self.assertEqual(actual_arr, expected_arr)

        char = 'n'
        actual_arr = c_lib.ctypes_update_guessed_index_array(expected_arr, char, word)
        expected_arr = [1, 1, 1, 1, 0, 0, 1, 1]
        self.assertEqual(actual_arr, expected_arr)

        char = 'a'
        actual_arr = c_lib.ctypes_update_guessed_index_array(expected_arr, char, word)
        expected_arr = [1, 1, 1, 1, 0, 1, 1, 1]
        self.assertEqual(actual_arr, expected_arr)

        char = 'h'
        actual_arr = c_lib.ctypes_update_guessed_index_array(expected_arr, char, word)
        expected_arr = [1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(actual_arr, expected_arr)
        arr = [0, 0, 0, 0, 0, 0, 0, 0]

        word = "computer"
        char = 'p'
        arr = [0, 0, 0, 0, 0, 0, 0, 0]
        actual_arr = c_lib.ctypes_update_guessed_index_array(arr, char, word)
        expected_arr = [0, 0, 0, 1, 0, 0, 0, 0]
        self.assertEqual(actual_arr, expected_arr)

        char = 'e'
        actual_arr = c_lib.ctypes_update_guessed_index_array(expected_arr, char, word)
        expected_arr = [0, 0, 0, 1, 0, 0, 1, 0]
        self.assertEqual(actual_arr, expected_arr)
        print("test_ctypes_update_guessed_index_array PASSED.")


    def test_ctypes_update_guessed_correctly(self):
        n = 10
        # test n updates
        n = c_lib.ctypes_update_guessed_correctly(n, 1)
        n = c_lib.ctypes_update_guessed_correctly(n, 1)
        self.assertEqual(n, 12)
        # test n does not update
        n = c_lib.ctypes_update_guessed_correctly(n, 0)
        self.assertEqual(n, 12)
        print("test_ctypes_update_guessed_correctly PASSED.")

    def test_ctypes_build_display_text(self):
        word = "prosperous"
        guessed_index_array = [1,0,0,0,1,0,0,0,0,0]
        expected_text = "p...p....."
        actual_text = c_lib.ctypes_build_display_text(
            guessed_index_array,
            word,
            len(word)
        )
        self.assertEqual(actual_text, expected_text)

        word = "laughs"
        guessed_index_array = [1,0,0,0,1,0]
        expected_text = "l...h."
        actual_text = c_lib.ctypes_build_display_text(
            guessed_index_array,
            word,
            len(word)
        )
        self.assertEqual(actual_text, expected_text)

        word = "magical"
        guessed_index_array = [1, 1, 1, 1, 1, 0, 1]
        expected_text = "magic.l"
        actual_text = c_lib.ctypes_build_display_text(
            guessed_index_array,
            word,
            len(word)
        )
        self.assertEqual(actual_text, expected_text)

        word = "magical"
        guessed_index_array = [1,1,1,1,1,1,1]
        expected_text = "magical"
        actual_text = c_lib.ctypes_build_display_text(
            guessed_index_array,
            word,
            len(word)
        )
        self.assertEqual(actual_text, expected_text)

        word = "magical"
        guessed_index_array = [1, 1, 1, 1, 1, 1, 1]
        expected_text = "magica."
        actual_text = c_lib.ctypes_build_display_text(
            guessed_index_array,
            word,
            len(word)
        )
        self.assertNotEqual(actual_text, expected_text)
        print("test_ctypes_build_display_text PASSED.")



if __name__ == '__main__':
    unittest.main()