## URLify

## Problem description

Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: if implementing in Java, please use a character array so that you can
perform this operation in place.)

## My solution and explanation

The solution I came up with is iterating through the string up to the size of the string,
assuming there are not white spaces in the start of the string and a single whitespace between
each word. The idea is to iterate through the string and replace every whitespace character with
`%20`, due to Python unable to reassign a character in a string's index, I used a list where I
append each character and join them.

```
def urlify(string, size):
    result = []
    for i in range(0, size):
        if string[i] == " ":
            result.append("%20")
        else:
            result.append(string[i])
    return "".join(result)
```

- Time complexity: O(N)
- Space complexity: O(N)

