# Check Permutation

## Problem description

Given two strings, write a method to decide if one is a permutation of the other.

## My solution and explanation

The solution I came up with uses two hash maps where we store each character of 
both strings in each hash map. First we check if the length of both strings are 
equal because if they are not of the same length then one string is not a 
permutation of the other. Then we compare both and if not the same we return `false`.

```
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
```

- Time complexity: O(N)
- Space complexity: O(N)
