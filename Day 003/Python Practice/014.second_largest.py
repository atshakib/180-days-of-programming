"""

### Problem 14: Find the Second Largest Number in a List

**Problem Statement**: Write a function that finds the second largest number in a list.

**Function Signature**: `def second_largest(numbers: list) -> int`

**Example**:
```python
assert second_largest([1, 2, 3, 4, 5]) == 4
assert second_largest([10, 20, 20, 5, 7]) == 10
assert second_largest([-1, -2, -3, -4]) == -2
```

### Instructions
1. Define the function `second_largest` with the specified signature.
2. The function should return the second largest number in the list `numbers`.
3. You can assume the list will contain at least two distinct numbers.

"""

def second_largest(numbers:list) -> int:
    largest = 0
    sec_largest = 0
    for number in numbers:
        if number > largest:
            largest = number
    numbers.remove(largest)
    for number in numbers:
        if number > sec_largest:
            sec_largest = number
    return sec_largest

try:
    n = int(input("How many numbers will there be in list? "))
    numbers = []
    print(f"Enter {n} numbers by clicking enter after each input: ")
    for i in range(n):
        numbers.append(int(input()))
    print(second_largest(numbers))
except ValueError:
    print("Enter valid integer input.")
