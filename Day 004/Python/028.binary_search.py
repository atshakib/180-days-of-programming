"""

### Problem 28: Implement Binary Search

**Problem Statement**: Implement the binary search algorithm to search for a target value in a sorted list of integers. If the target is found, return its index; otherwise, return -1.

**Function Signature**: `def binary_search(arr: list, target: int) -> int`

**Example**:
```python
assert binary_search([2, 3, 5, 7, 11, 13, 17], 11) == 4
assert binary_search([1, 2, 3, 4, 5], 6) == -1
```

### Required Topics:
1. **Lists/Arrays**: Manipulation of lists or arrays in Python.
2. **Looping Constructs**: Use of loops (e.g., `while` loop) to perform iterations.
3. **Conditional Statements**: Use of conditional statements (e.g., `if`, `else`) for comparisons.
4. **Mathematical Concepts**: Understanding of the binary search algorithm and its underlying principles.

"""



def binary_search(arr: list, target: int) -> int:
    start = 0
    end = len(arr)-1
    
    while start <= end:
        mid = start + (end - start) // 2 
        if(target == arr[mid]):
            return mid
        elif(target < arr[mid]):
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(binary_search([2, 3, 5, 7, 11, 13, 17], 11))
