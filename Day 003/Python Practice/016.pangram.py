"""

### Problem 16: Check if a String is a Pangram

**Problem Statement**: Write a function that checks whether a given string is a pangram or not.

**Function Signature**: `def is_pangram(s: str) -> bool`

**Example**:
```python
assert is_pangram("The quick brown fox jumps over the lazy dog") == True
assert is_pangram("This is not a pangram") == False
```

### Instructions
1. Define the function `is_pangram` with the specified signature.
2. The function should return `True` if the input string `s` is a pangram, and `False` otherwise.
3. A pangram is a string that contains every letter of the alphabet at least once.

"""

def is_pangram(s:str) -> bool:
    char = 'abcdefghijklmnopqrstuvwxyz'
    for letter in char:
        if letter not in s:
            return False
    return True

s = input("Enter your string : ")
print(is_pangram(s))