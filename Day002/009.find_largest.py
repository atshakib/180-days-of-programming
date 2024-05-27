"""

### Problem 9: Find the Largest Element in a List

**Problem Statement**: Write a function that returns the largest element in a given list of numbers.

**Function Signature**: `def find_largest(numbers: list) -> int`

**Example**:
```python
assert find_largest([1, 2, 3, 4, 5]) == 5
assert find_largest([10, 20, 5, 7]) == 20
assert find_largest([-1, -2, -3, -4]) == -1
```

### Instructions
1. Define the function `find_largest` with the specified signature.
2. The function should return the largest number in the list `numbers`.
3. You can assume the list will contain at least one number.

"""

def find_largest(numbers: list) -> int:
    largest = 0
    for number in numbers:
        if number > largest:
            largest = number
    return largest

try:
    numbers = []
    n = int(input("How many element will there be in your list? "))
    print(f"Enter {n} numbers by pressing 'enter' after every input: ")
    for i in range(0,n):
        ele = int(input())
        numbers.append(ele)
    print(find_largest(numbers))
except ValueError:
    print("Enter only integers as input.")