"""

### Problem 22: Find the Most Frequent Element in a List

**Problem Statement**: Write a function that finds the most frequent element in a list. If there are multiple elements with the same highest frequency, return any one of them.

**Function Signature**: `def most_frequent(lst: list) -> any`

**Example**:
```python
assert most_frequent([1, 2, 2, 3, 3, 3, 4]) == 3
assert most_frequent(['a', 'b', 'b', 'c', 'a', 'a']) == 'a'
```

### Instructions
1. Define the function `most_frequent` with the specified signature.
2. The function should return the element that appears most frequently in the list.
3. If there are ties, return any one of the most frequent elements.

Try to solve this problem on your own. When you’re ready, you can share your solution, and we can review it and proceed to the next problem.

"""

def most_frequent(lst: list) -> int:
    if not lst:
        return None  # Return None or raise an exception for an empty list
    
    frequency = {}
    max_count = 0
    most_frequent_element = lst[0]

    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

        if frequency[item] > max_count:
            max_count = frequency[item]
            most_frequent_element = item

    return most_frequent_element

# Test case
print(most_frequent([1, 2, 2, 3, 1]))  # Expected: 2
