"""

### Problem 26: Implement Selection Sort

**Problem Statement**: Implement the selection sort algorithm to sort a list of integers in non-decreasing order.

**Function Signature**: `def selection_sort(arr: list) -> list`

**Example**:
```python
assert selection_sort([5, 2, 4, 6, 1, 3]) == [1, 2, 3, 4, 5, 6]
```

### Required Topics:
1. **Sorting Algorithms**: Understanding of the selection sort algorithm.
2. **Lists/Arrays**: Manipulation of lists or arrays in Python.
3. **Looping Constructs**: Use of loops (e.g., `for` loop) to iterate over elements.
4. **Conditional Statements**: Use of conditional statements (e.g., `if`) for comparisons.

"""


def selection_sort(arr: list) -> list:
    for i in range(len(arr) - 1):
        index_of_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index_of_min]:
                index_of_min = j
        arr[i], arr[index_of_min] = arr[index_of_min], arr[i]
    return arr

print(selection_sort([5, 2, 4, 6, 1, 3]))