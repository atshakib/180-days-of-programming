import re

def magicOrNot(n: int) -> str:
    # Convert the integer to a string
    n_str = str(n)
    # Regular expression to match the magic number pattern
    pattern = re.compile(r'^(1|14|144)+$')
    if pattern.match(n_str):
        return "YES"
    else:
        return "NO"

# Read the input as an integer
n = int(input())
print(magicOrNot(n))
