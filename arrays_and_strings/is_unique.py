import unittest

# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?
def is_unique(string):
    characters = {}
    for char in string:
        if char in characters:
            return False
        characters[char] = char
    return True

class TestIsUnique(unittest.TestCase):
    def test_is_true(self):
        self.assertTrue(is_unique('abcd'))
        self.assertTrue(is_unique('abc'))
        self.assertTrue(is_unique('b'))
        self.assertTrue(is_unique('zyskeihg'))
        self.assertTrue(is_unique('helmotaugdrsi'))

    def test_is_false(self):
        self.assertFalse(is_unique('aabd'))
        self.assertFalse(is_unique('abbdde'))
        self.assertFalse(is_unique('aa'))
        self.assertFalse(is_unique('hellomotto'))
        self.assertFalse(is_unique('moto'))

if __name__ == "__main__":
    unittest.main() 

