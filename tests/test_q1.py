"""Tests for Lab 0 Question 1"""

import unittest
from unittest.mock import patch, Mock
from src.q1 import is_palindrome

def check_user_input() -> bool:
    s = input("Enter a string: ")
    return is_palindrome(s)

class TestIsPalindrome(unittest.TestCase):

    @patch('builtins.input', side_effect=['aa'])
    def test_palindrome(self, _: Mock) -> None:
        self.assertTrue(check_user_input())

    @patch('builtins.input', side_effect=['ab'])
    def test_not_palindrome(self, _: Mock) -> None:
        self.assertFalse(check_user_input())

if __name__ == "__main__":
    unittest.main()