"""

### Problem 25: Implement Insertion Sort

**Problem Statement**: Implement the insertion sort algorithm to sort a list of integers in non-decreasing order.

**Function Signature**: `def insertion_sort(arr: list) -> list`

**Example**:
```python
assert insertion_sort([5, 2, 4, 6, 1, 3]) == [1, 2, 3, 4, 5, 6]
```

### Required Topics:
1. **Sorting Algorithms**: Understanding of the insertion sort algorithm.
2. **Lists/Arrays**: Manipulation of lists or arrays in Python.
3. **Looping Constructs**: Use of loops (e.g., `for` loop) to iterate over elements.
4. **Conditional Statements**: Use of conditional statements (e.g., `if`) for comparisons.

"""

def insertion_sort(arr: list) -> list:
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr

print(insertion_sort([5, 2, 4, 6, 1, 3]))
    

