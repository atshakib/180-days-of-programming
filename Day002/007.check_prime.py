"""

### Problem 7: Prime Number Check

**Problem Statement**: Write a function that checks if a given integer is a prime number.

**Function Signature**: `def is_prime(n: int) -> bool`

**Example**:
```python
assert is_prime(7) == True
assert is_prime(10) == False
assert is_prime(1) == False
```

### Instructions
1. Define the function `is_prime` with the specified signature.
2. The function should return `True` if the input integer `n` is a prime number, and `False` otherwise.
3. A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.

"""


def if_prime(n: int) -> bool:
    if n <= 0:
        raise ValueError("Please enter a positive number.")
    for i in range(2,n):
        if n%i==0:
            return False
    return True

try: 
    n = int(input("Enter the number you want to check: "))
    print(if_prime(n))
except ValueError:
    print("Please enter a positive number.")