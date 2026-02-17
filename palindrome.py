"""
Validates strings as palindromes.
"""
from collections import deque


def is_palindrome(value: str) -> bool:
    """Checks if the given string value is a palindrome."""
    if not isinstance(value, str):
        raise TypeError("Input must be a string.")
    
    standardized_value = "".join(char.lower() for char in value if char.isalnum())

    if standardized_value == "":
        return False
    
    deq = deque(standardized_value)

    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False
    
    return True