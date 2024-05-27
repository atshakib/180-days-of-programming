"""

### Problem 8: Reverse a String

**Problem Statement**: Write a function that reverses a given string.

**Function Signature**: `def reverse_string(s: str) -> str`

**Example**:
```python
assert reverse_string("hello") == "olleh"
assert reverse_string("OpenAI") == "IAnepO"
assert reverse_string("Python") == "nohtyP"
```

### Instructions
1. Define the function `reverse_string` with the specified signature.
2. The function should return the input string `s` reversed.

"""

def reverse_string(s: str) -> str:
    if s <= 1:
        return s
    return s[::-1]

s = input("Enter the string: ")
print(reverse_string(s))