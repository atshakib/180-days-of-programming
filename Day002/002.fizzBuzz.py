"""

### Problem 2: FizzBuzz

**Problem Statement**: Write a function that prints the numbers from 1 to `n`. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".

**Function Signature**: `def fizz_buzz(n: int) -> None:`

**Example**:

fizz_buzz(15)

**Expected Output**:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz

### Instructions
1. Define the function `fizz_buzz` with the specified signature.
2. The function should print the numbers from 1 to `n` with the specified substitutions.
3. Test the function with different values of `n`.

"""


def fizz_buzz(n:int) -> int:
    for i in range(1,n+1):
        if(i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        else:
            print(i)

try:
    n = int(input("Enter the last number: "))
    fizz_buzz(n)
except ValueError:
    print("Enter a valid input please.")