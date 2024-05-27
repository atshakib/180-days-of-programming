"""

### Problem 5: Fibonacci Sequence

**Problem Statement**: Write a function that returns the n-th Fibonacci number. The Fibonacci sequence is defined as follows:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1

**Function Signature**: `def fibonacci(n: int) -> int`

**Example**:
```python
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(5) == 5
assert fibonacci(10) == 55
```

### Instructions
1. Define the function `fibonacci` with the specified signature.
2. The function should return the n-th Fibonacci number.
3. Implement the function using an iterative approach to handle larger values of `n` efficiently.

"""


def fibonacci(n: int) -> int:
    if n<0:
        raise ValueError("Input cannot be a negative number!")
    elif n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

try:
    n = int(input("Enter the number: "))
    print(fibonacci(n))
except ValueError:
    print("Please enter a valid input")
    