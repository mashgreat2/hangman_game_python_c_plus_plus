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

    # add more tests here.


if __name__ == '__main__':
    unittest.main()