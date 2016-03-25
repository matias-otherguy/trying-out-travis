import unittest
from random import choice
from string import ascii_letters

from a_module import remove_vowels

class TestThings(unittest.TestCase):
    
    def test_remove_vowels_does_not_return_vowels(self):
        vowels = ("a", "e", "i",
                  "o", "u", "y" )
        a_str = ''.join(choice(ascii_letters) for _ in range(10000))
        for c in remove_vowels(a_str):
            self.assertFalse(str.lower(c) in vowels, "Found vowel in string")
