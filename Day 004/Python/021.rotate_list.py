"""

### Problem 21: Rotate a List

**Problem Statement**: Write a function that rotates the elements of a list to the right by a given number of steps.

**Function Signature**: `def rotate_list(lst: list, k: int) -> list`

**Example**:
```python
assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
assert rotate_list([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]  # Note: 7 % 5 == 2
```

### Instructions
1. Define the function `rotate_list` with the specified signature.
2. The function should return a new list with elements rotated to the right by `k` steps.
3. Handle cases where `k` is larger than the length of the list by using modulo operation.

"""

def rotate_list(lst: list, k: int) -> list:
    n = len(lst)
    k = k % n  # Correctly calculate k within the bounds of the list length
    return lst[-k:] + lst[:-k]  # Slice the list to rotate to the right

# Test case
print(rotate_list([1, 2, 3, 4, 5], 2))  # Expected: [4, 5, 1, 2, 3]
