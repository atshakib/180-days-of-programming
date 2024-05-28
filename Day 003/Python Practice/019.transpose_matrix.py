"""

### Problem 19: Matrix Transposition

**Problem Statement**: Write a function that transposes a given 2D matrix. The transpose of a matrix is obtained by swapping the rows and columns.

**Function Signature**: `def transpose_matrix(matrix: list) -> list`

**Example**:
```python
assert transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
assert transpose_matrix([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]
```

### Instructions
1. Define the function `transpose_matrix` with the specified signature.
2. The function should return the transposed matrix.
3. The input matrix is a list of lists, where each inner list represents a row of the matrix.

"""


def transpose_matrix(matrix):
  transpose = []
  for col in range(len(matrix[0])):
    new_row = []
    for row in range(len(matrix)):
      new_row.append(matrix[row][col])
    transpose.append(new_row)
  return transpose

print(transpose_matrix([[1, 2], [3, 4], [5, 6]]))
