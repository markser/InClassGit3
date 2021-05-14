import io
import sys
import unittest
from unittest.mock import patch
import wordCount

# run with python3 command 
# python3 testWordCount.py

class TestWordCount(unittest.TestCase):
    @patch('builtins.input', side_effect=['This is an activity'])
    def test_normal_values(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        wordCount.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['4', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)
    
    @patch('builtins.input', side_effect=[''])
    def test_empty_string(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        wordCount.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['0', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)
    
    @patch('builtins.input', side_effect=['This  is  an  activity'])
    def test_normal_values_with_double_space(self,mock_input):
        # with unittest.mock.patch('volumeOfCube.retrieve_input', return_value=-1):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        wordCount.main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        expected = ['4', '']
        actual = capturedOutput.getvalue().split('\n')
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()