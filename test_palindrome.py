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