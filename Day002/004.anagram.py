"""

### Problem 4: Anagram Check

**Problem Statement**: Write a function that checks if two given strings are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once (ignoring spaces, punctuation, and capitalization).

**Function Signature**: `def are_anagrams(s1: str, s2: str) -> bool`

**Example**:
```
assert are_anagrams("listen", "silent") == True
assert are_anagrams("triangle", "integral") == True
assert are_anagrams("apple", "pale") == False
```

### Instructions
1. Define the function `are_anagrams` with the specified signature.
2. The function should return `True` if the two input strings `s1` and `s2` are anagrams, and `False` otherwise.
3. Ignore spaces, punctuation, and capitalization while checking for anagrams.

"""


def are_anagrams(s1: str , s2: str) -> bool:
    s1_cleaned = ''.join(char.lower() for char in s1 if char.isalnum())
    s2_cleaned = ''.join(char.lower() for char in s2 if char.isalnum())

    if(len(s1_cleaned) != len(s2_cleaned)):
        return False
    else:
        return sorted(s1_cleaned) == sorted(s2_cleaned)

try:
    s1 = input("Enter first word: ")
    s2 = input("Enter second word: ")
    print(are_anagrams(s1,s2))
except:
    print("Enter valid input.")

           
