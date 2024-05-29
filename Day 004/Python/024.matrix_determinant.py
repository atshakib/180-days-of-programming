"""

### Problem 24: Calculate the Determinant of a Square Matrix

**Problem Statement**: Write a function to calculate the determinant of a square matrix. The function should take a square matrix (2D list) as input and return its determinant. Assume the matrix is non-empty and square.

**Function Signature**: `def determinant(matrix: list) -> float`

**Example**:
```python
assert determinant([[1, 2], [3, 4]]) == -2.0
assert determinant([[2, 5, 3], [1, -2, -1], [1, 3, 4]]) == -20.0
```

### Required Topics:
1. **Matrix Manipulation**: You need to understand how to access elements of a matrix and perform operations like addition, subtraction, and multiplication.
2. **Recursion**: Calculating the determinant involves recursive calls to find determinants of smaller matrices.
3. **Mathematical Concepts**: You should be familiar with concepts such as cofactor expansion and the properties of determinants.

"""

def determinant(matrix: list) -> float:
    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols:
        raise ValueError("Matrix must be square for determinant calculation.")

    if rows == 1:
        return matrix[0][0]
    elif rows == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for j in range(cols):
            minor = [row[:j] + row[j+1:] for row in matrix[1:]]
            det += matrix[0][j] * (-1) ** j * determinant(minor)
        return det

# Test cases
print(determinant([[1, 2], [3, 4]]))  # Expected: -2
print(determinant([[2, 5, 3], [1, -2, -1], [1, 3, 4]]))  # Expected: 5
print(determinant([[3]]))  # Expected: 3


