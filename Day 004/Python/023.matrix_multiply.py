def matrix_multiply(mat1: list, mat2: list) -> list:
  rows1 = len(mat1)
  cols1 = len(mat1[0])
  rows2 = len(mat2)
  cols2 = len(mat2[0])

  if cols1 != rows2:
    raise ValueError("Matrices must have compatible dimensions for multiplication.")

  result = [[0 for _ in range(cols2)] for _ in range(rows1)]

  for i in range(rows1):
    for j in range(cols2):
      for k in range(cols1):  
        result[i][j] += mat1[i][k] * mat2[k][j]

  return result

assert matrix_multiply(
  [[1, 2],
   [3, 4]],
  [[5, 6],
   [7, 8]]
) == [[19, 22],
    [43, 50]]
print(matrix_multiply([[1, 0], [2, 1]], [[4, 2], [3, 1]]))  
