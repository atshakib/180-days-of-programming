"""

### Problem 12: Merge Two Sorted Lists

**Problem Statement**: Write a function that merges two sorted lists into a single sorted list.

**Function Signature**: `def merge_sorted_lists(list1: list, list2: list) -> list`

**Example**:
```python
assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
assert merge_sorted_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]
assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]
```

### Instructions
1. Define the function `merge_sorted_lists` with the specified signature.
2. The function should return a single sorted list containing all elements from `list1` and `list2`.
3. Both input lists are assumed to be sorted in ascending order.

"""

def merge_sorted_lists(list1: list , list2 : list) -> list:
    merged_list = []
    for numbers in list1:
        merged_list.append(numbers)
    for number in list2:
        merged_list.append(number)
    return sorted(merged_list)

n = int(input("How many elements will there be in list 1? "))
print(f"Enter {n} number by pressing enter after each input:")
list1 = []
for i in range(n):
    list1.append(input())

m = int(input("How many elements will there be in list 2? "))
print(f"Enter {m} number by pressing enter after each input:")
list2 = []
for i in range(m):
    list2.append(input())

print(merge_sorted_lists(sorted(list1) , sorted(list2)))



# def merge_sorted_lists(list1: list, list2: list) -> list:
#     merged_list = []
#     i, j = 0, 0
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             merged_list.append(list1[i])
#             i += 1
#         else:
#             merged_list.append(list2[j])
#             j += 1
#     merged_list.extend(list1[i:])
#     merged_list.extend(list2[j:])
#     return merged_list

# try:
#     n = int(input("How many elements will there be in list 1? "))
#     print(f"Enter {n} numbers by pressing enter after each input:")
#     list1 = [int(input()) for _ in range(n)]

#     m = int(input("How many elements will there be in list 2? "))
#     print(f"Enter {m} numbers by pressing enter after each input:")
#     list2 = [int(input()) for _ in range(m)]

#     print(merge_sorted_lists(list1, list2))
# except ValueError:
#     print("Please enter valid integers.")
