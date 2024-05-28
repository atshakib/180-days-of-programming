"""

### Problem 11: Count Occurrences of a Character in a String

**Problem Statement**: Write a function that counts the number of times a given character appears in a string.

**Function Signature**: `def count_occurrences(s: str, char: str) -> int`

**Example**:
```python
assert count_occurrences("hello", "l") == 2
assert count_occurrences("OpenAI", "e") == 1
assert count_occurrences("Python", "p") == 0
```

### Instructions
1. Define the function `count_occurrences` with the specified signature.
2. The function should return the count of how many times `char` appears in the string `s`.
3. The search should be case-sensitive (e.g., 'a' and 'A' should be counted separately).

"""
def count_occurrences(s: str, char:str)->int:
    count = 0
    for ch in s:
        if ch == char:
            count += 1
    return count

s = input("Enter your string: ")
char = input("Enter the character you want to search: ")
print(count_occurrences(s,char))