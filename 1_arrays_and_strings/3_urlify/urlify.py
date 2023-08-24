import unittest

# URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the 
# additional characters, and that you are given the "true" length of the string. 
# (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith    " 13
# Output: "Mr%20John%20Smith" 

def urlify(string, size):
    result = []
    for i in range(0, size):
        if string[i] == " ":
            result.append("%20")
        else:
            result.append(string[i])
    return "".join(result)

class TestURLify(unittest.TestCase):
    TEST_DATA = [
            ('Mr John Smith    ', 13, 'Mr%20John%20Smith')

    ]

    def test_urlify(self):
        for string_input, size_input, expected_result in self.TEST_DATA:
            result = urlify(string_input, size_input)
            self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
