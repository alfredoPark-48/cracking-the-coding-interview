# Is Unique
## Problem description
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures? 

## My solution and explanation
The idea behind my implementation is to use a hash map/dictionary in order to store each character of the string.
We iterate through the input string and check if a character already exists in the hash map.
If we already have a character in the hash map then we return `false` because we have duplicate characters, therefore the string does not have unique characters.
If we finished iterating through the string then we return `true` since the `if` condition was never executed, therefore our input string has unique characters.

```
def is_unique(string):
    characters = {}
    for char in string:
        if char in characters:
            return False
        characters[char] = char
    return True
```

- Time complexity: O(N)
- Space complexity: O(N)

