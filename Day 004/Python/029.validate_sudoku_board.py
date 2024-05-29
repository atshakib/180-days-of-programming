"""

### Problem 29: Validate Sudoku Board

**Problem Statement**: Given a 9x9 matrix representing a sudoku board, write a function to determine if the board is valid. The board is valid if all rows, columns, and 3x3 subgrids contain the digits 1-9 without repetition.

**Function Signature**: `def is_valid_sudoku(board: list) -> bool`

**Example**:
```python
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
assert is_valid_sudoku(board) == True
```

### Required Topics:
1. **Lists/Arrays**: Manipulation of lists or arrays in Python.
2. **Nested Loops**: Use of nested loops (e.g., `for` loop inside another `for` loop) to traverse elements of a 2D array.
3. **Sets**: Utilization of sets to check for uniqueness of digits.
4. **Conditional Statements**: Use of conditional statements (e.g., `if`, `else`) for comparisons.

"""

def is_valid_sudoku(board: list) -> bool:
    #check rows
    for row in board:
        seen = set()
        for num in row:
            if num != "." and num in seen:
                return False
            seen.add(num)
    

    #check columns
    for col in range(len(board)):
        seen = set()
        for row in range(len(board)):
            num = board[row][col]
            if num != "." and num in seen:
                return False
            seen.add(num)
    

    #check subgrids
    subgrid_size = int(len(board)**0.5)
    for row_start in range(0, len(board), subgrid_size):
        for col_start in range(0, len(board), subgrid_size):
            seen = set()
            for row in range(row_start, row_start + subgrid_size):
                for col in range(col_start, col_start + subgrid_size):
                    num = board[row][col]
                    if num != "." and num in seen:
                        return False
                    seen.add(num)
    return True


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(is_valid_sudoku(board))
board_invalid = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(is_valid_sudoku(board_invalid))  # Should print False
