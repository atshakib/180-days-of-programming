"""

### Problem 15: Calculate the Factorial of a Number

**Problem Statement**: Write a function that calculates the factorial of a given non-negative integer.

**Function Signature**: `def factorial(n: int) -> int`

**Example**:
```python
assert factorial(5) == 120
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(3) == 6
```

### Instructions
1. Define the function `factorial` with the specified signature.
2. The function should return the factorial of the input integer `n`.
3. The factorial of `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`.

"""

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Negative number does not have a factorial.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    n = int(input("Enter the number: "))
    print(factorial(n))
except ValueError as e:
    print(e)
