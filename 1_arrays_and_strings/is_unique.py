import unittest

# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

# For this implementation I used a hashmap/dictionary in order to store each
# character, if there is already a character in the dictionary we can therefore
# say that a string is not unique.

# Run time O(N)
# Space complexity O(N)
def is_unique(string):
    characters = {}
    for char in string:
        if char in characters:
            return False
        characters[char] = char
    return True

# I could not come up with a solution running in O(N) time without the use of
# an additional data structure, after reviewing the solution given by the book
# we can iterate through each character of the string and use a count method 
# to check if there is more than one character in the string, if has then we
# return false

# Run time complexity O(N)
# Space time complexity O(1)
def is_unique_no_data_structure(string):
    for char in string:
        if string.count(char) > 1:
            return False
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

def test_no_duplicates_both_versions(self):
        for string, expected_result in self.TEST_DATA:
            result1 = is_unique(string)
            self.assertEqual(result1, expected_result)

            # Test the version without additional data structures too
            result2 = is_unique_no_data_structure(string)
            self.assertEqual(result2, expected_result)

if __name__ == "__main__":
    unittest.main() 

