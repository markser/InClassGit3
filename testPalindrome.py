import io
import sys
import unittest
from unittest.mock import patch
import palindrome
# run with python3 command 
# python3 testPalindrome.py.py

class TestCalculator(unittest.TestCase):
    @patch('builtins.input', side_effect=['Thisisanactivity'])
    def test_bad_string(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        palindrome.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['False', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)
    
    @patch('builtins.input', side_effect=[''])
    def test_empty_string(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        palindrome.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['True', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)
    
    @patch('builtins.input', side_effect=['tacocat'])
    def test_valid_string(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        palindrome.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['True', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['tAcOcAt'])
    def test_valid_string_alternating_capitalized_letters(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        palindrome.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['True', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()