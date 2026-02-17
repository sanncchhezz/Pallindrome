"""
Tests the palindrome module
"""
from palindrome import is_palindrome
import pytest

def test_palindrome_not_string():
    """Tests that a TypeError is raised when the input is not a string."""
    with pytest.raises(TypeError):
        is_palindrome(123)