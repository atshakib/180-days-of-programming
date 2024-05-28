"""

### Problem 20: Remove Duplicates from a List

**Problem Statement**: Write a function that removes duplicates from a list while maintaining the original order of elements.

**Function Signature**: `def remove_duplicates(lst: list) -> list`

**Example**:
```python
assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
assert remove_duplicates(['a', 'b', 'a', 'c', 'b']) == ['a', 'b', 'c']
assert remove_duplicates([1, 1, 1, 1]) == [1]
```

### Instructions
1. Define the function `remove_duplicates` with the specified signature.
2. The function should return a list with duplicates removed, maintaining the original order.
3. You can use a set to keep track of seen elements and a list to store the result.

"""


#by looping
def remove_duplicates(lst: list) -> list:
    new_lst = []
    for char in lst:
        if char not in new_lst:
            new_lst.append(char)
    return new_lst

#by using set
def remove_duplicates(lst: list) -> list:
    seen = set()
    new_lst = []
    for item in lst:
        if item not in seen:
            new_lst.append(item)
            seen.add(item)
    return new_lst

# Test cases
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Expected: [1, 2, 3, 4, 5]
print(remove_duplicates(['a', 'b', 'a', 'c', 'b']))  # Expected: ['a', 'b', 'c']
print(remove_duplicates([1, 1, 1, 1]))  # Expected: [1]
print(remove_duplicates([]))  # Expected: []
print(remove_duplicates(['x', 'y', 'z', 'x', 'y']))  # Expected: ['x', 'y', 'z']
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))