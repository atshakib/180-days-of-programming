"""

### Problem 17: Find All Prime Numbers up to a Given Number

**Problem Statement**: Write a function that finds all prime numbers up to a given integer `n`.

**Function Signature**: `def find_primes(n: int) -> list`

**Example**:
```python
assert find_primes(10) == [2, 3, 5, 7]
assert find_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
```

### Instructions
1. Define the function `find_primes` with the specified signature.
2. The function should return a list of all prime numbers less than or equal to `n`.
3. You can use the Sieve of Eratosthenes algorithm for an efficient solution.

"""

def find_primes(n: int) -> list:
    if(n < 0):
        raise ValueError("Enter a positive number kindly.")
    primes = []
    for i in range(2,n+1):
        is_prime = True
        for j in range(2,i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes
try:
    n = int(input("Enter n: "))
    print(find_primes(n))
except ValueError:
    print("Enter a valid number.")
