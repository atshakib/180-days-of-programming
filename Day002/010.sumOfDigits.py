"""

### Problem 10: Sum of Digits

**Problem Statement**: Write a function that takes an integer as input and returns the sum of its digits.

**Function Signature**: `def sum_of_digits(n: int) -> int`

**Example**:
```python
assert sum_of_digits(123) == 6
assert sum_of_digits(456) == 15
assert sum_of_digits(789) == 24
```

### Instructions
1. Define the function `sum_of_digits` with the specified signature.
2. The function should return the sum of the digits of the input integer `n`.

"""


def sum_of_digits(n: int)->int:
    if n<0:
        raise ValueError("Enter a positive number.")
    sum = 0
    for num in str(n):
        sum += int(num)
    return sum

try:
    n = int(input("Enter the number: "))
    print(sum_of_digits(n))
except ValueError:
    print("Enter a valid input.")