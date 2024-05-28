"""

### Problem 3: Palindrome Check

**Problem Statement**: Write a function that checks if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

**Function Signature**: `def is_palindrome(s: str) -> bool`

**Example**:
```
assert is_palindrome("A man, a plan, a canal, Panama") == True
assert is_palindrome("racecar") == True
assert is_palindrome("hello") == False
```

### Instructions
1. Define the function `is_palindrome` with the specified signature.
2. The function should return `True` if the input string `s` is a palindrome, and `False` otherwise.
3. Ignore spaces, punctuation, and capitalization while checking for palindrome.

"""

def rev(s: str) -> str:
    return s[::-1]

def is_palindrome(s: str) -> bool:
    result = []
    for char in s:
        if char.isalnum(): 
            result.append(char.lower())  

    cleaned_string = ''.join(result)
    return cleaned_string == rev(cleaned_string)

try:
    s = input("Enter your string: ")
    print(is_palindrome(s))
except ValueError:
    print("Please enter a valid string")
