"""

### Problem 18: Find the Length of the Longest Word in a Sentence

**Problem Statement**: Write a function that finds the length of the longest word in a given sentence.

**Function Signature**: `def longest_word_length(sentence: str) -> int`

**Example**:
```python
assert longest_word_length("The quick brown fox jumps over the lazy dog") == 5
assert longest_word_length("A journey of a thousand miles begins with a single step") == 8
assert longest_word_length("To be or not to be that is the question") == 8
```

### Instructions
1. Define the function `longest_word_length` with the specified signature.
2. The function should return the length of the longest word in the input string `sentence`.
3. Assume words are separated by spaces.

"""

def longest_word_length(sentence : str) -> int:
    count = 0
    word = sentence.split()
    for char in word:
        if len(char) > count:
            count = len(char)
    return count

sentence = input("Enter your sentence: ")
print(longest_word_length(sentence))