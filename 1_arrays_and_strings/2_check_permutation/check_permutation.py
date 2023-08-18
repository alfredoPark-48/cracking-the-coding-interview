import unittest

# Time complexity O(N)
# Space complexity O(N)
def check_permutations(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        char_map1 = {}
        char_map2 = {}

        for char in string1:
            if char in char_map1:
                char_map1[char] += 1
            else:
                char_map1[char] = 1

        for char in string2:
            if char in char_map2:
                char_map2[char] += 1
            else:
                char_map2[char] = 1

        return char_map1 == char_map2
     

class CheckPermutationTest(unittest.TestCase):
    TEST_DATA = [
            ('aba', 'baa', True),
            ('abac', 'cbaa', True),
            ('aba', 'baab', False),
            ('cat', 'tac', True),
            ('amehane', 'haneane', False),
            ('namejame', 'jamename', True)
    ]

    def test(self):
        for string1, string2, expected in self.TEST_DATA:
            test_result = check_permutations(string1, string2)
            self.assertEqual(test_result, expected)

if __name__ == "__main__":
   unittest.main() 
