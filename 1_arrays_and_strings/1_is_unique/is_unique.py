import unittest

def is_unique(string):
    characters = {}
    for char in string:
        if char in characters:
            return False
        characters[char] = char
    return True

class TestIsUnique(unittest.TestCase):
    TEST_DATA = [
            ('a', True),
            ('aa', False),
            ('ab', True),
            ('ab ', True),
            ('', True),
            (' ', True),
            ('  ', False),
            ('qwerty', True),
            ('qwerte', False)]

    def test_is_unique(self):
        for string, expected_result in self.TEST_DATA:
            result1 = is_unique(string)
            self.assertEqual(result1, expected_result)

if __name__ == "__main__":
    unittest.main() 

