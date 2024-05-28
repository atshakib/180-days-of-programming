"""

### Problem 13: Find the GCD of Two Numbers

**Problem Statement**: Write a function that computes the greatest common divisor (GCD) of two integers.

**Function Signature**: `def find_gcd(a: int, b: int) -> int`

**Example**:
```python
assert find_gcd(54, 24) == 6
assert find_gcd(48, 18) == 6
assert find_gcd(101, 103) == 1
```

### Instructions
1. Define the function `find_gcd` with the specified signature.
2. The function should return the GCD of the input integers `a` and `b`.
3. You can use the Euclidean algorithm to compute the GCD.

"""

def gcd(a:int , b:int) -> int:
    while b!=0 :
        rem = a % b
        a = b
        b = rem
    return a

try: 
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(gcd(a,b))
except ValueError:
    print("Enter a valid input.")