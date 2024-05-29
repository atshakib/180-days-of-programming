"""

### Problem 27: Find the Longest Common Prefix

**Problem Statement**: Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

**Function Signature**: `def longest_common_prefix(strs: list) -> str`

**Example**:
```python
assert longest_common_prefix(["flower","flow","flight"]) == "fl"
assert longest_common_prefix(["dog","racecar","car"]) == ""
```

### Required Topics:
1. **Strings**: Understanding of string manipulation in Python.
2. **Lists/Arrays**: Manipulation of lists or arrays in Python.
3. **Looping Constructs**: Use of loops (e.g., `for` loop) to iterate over elements.
4. **Conditional Statements**: Use of conditional statements (e.g., `if`) for comparisons.

"""

def longest_common_prefix(strs: list) -> str:
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for other in strs:
            if i == len(other) or other[i] != char:
                return shortest[:i]
    return shortest

print(longest_common_prefix(["flower","flow","flight"]))