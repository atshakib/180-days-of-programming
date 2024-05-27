"""

### Problem 6: Count Vowels

**Problem Statement**: Write a function that counts the number of vowels (a, e, i, o, u) in a given string.

**Function Signature**: `def count_vowels(s: str) -> int`

**Example**:
```python
assert count_vowels("hello") == 2
assert count_vowels("OpenAI") == 3
assert count_vowels("xyz") == 0
```

### Instructions
1. Define the function `count_vowels` with the specified signature.
2. The function should return the count of vowels in the input string `s`.
3. The function should be case-insensitive (i.e., count both uppercase and lowercase vowels).

"""


def count_vowels(s: str) -> int:
    count = 0
    for char in s:
        if char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u':
            count+=1
        else:
            continue
    return count

s = input("Enter your string: ")
print(count_vowels(s))