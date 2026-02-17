"""
Tests the palindrome module
"""
from palindrome import is_palindrome
import pytest

def test_palindrome_not_string():
    """Tests that a TypeError is raised when the input is not a string."""
    with pytest.raises(TypeError):
        is_palindrome(123)

def test_palindrome_empty_string():
    """Tests that an empty string is not considered a palindrome."""
    assert is_palindrome("") == False

def test_palindrome_valid_with_single_char():
    """Tests that a single character string is considered a palindrome."""
    assert is_palindrome("a") == True

def test_palindrome_valid_with_two_same_chars():
    """Tests that a string with two identical characters is considered a palindrome."""
    assert is_palindrome("bb") == True

def test_palindrome_invalid_with_different_chars():
    """Tests that a string with two different characters is not considered a palindrome."""
    assert is_palindrome("abc") == False

def test_palindrome_valid_laval():
    """Tests that the string 'laval' is considered a palindrome."""
    assert is_palindrome("laval") == True

def test_palindrome_invalid_toronto():
    """Tests that the string 'toronto' is not considered a palindrome."""
    assert is_palindrome("toronto") == False