"""

Problem 1: Sum of Two Numbers

Problem Statement: Write a function that takes two integers as input and returns their sum.

Function Signature: def sum_two_numbers(a: int, b: int) -> int:

Example:
assert sum_two_numbers(3, 4) == 7
assert sum_two_numbers(-1, 5) == 4


Instructions
1. Define the function sum_two_numbers with the specified signature.
2. The function should return the sum of the two input integers.
3. Test the function with the provided example inputs.

"""


def sumOfTwo(num1, num2):
    return num1 + num2
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
print(sumOfTwo(num1, num2))