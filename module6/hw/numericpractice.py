import numeric

def is_zero(matrix):
    """
    Check if all entries of a matrix are 0.

    Inputs:
      matrix - a numeric matrix

    Returns:
      True if all entries of the matrix are 0,
      False otherwise.
    """
    
    for i in range(len(matrix)):
        for l in range(len(matrix[0])):
            if matrix[i][l] != 0:
                return False
            
    return True

"""
matrix = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
print(is_zero(matrix))
"""

def are_equal(matrix1, matrix2):
    """
    Check if the two matrices are equal.

    Inputs:
      matrix1 - a numeric matrix
      matrix2 - a numeric matrix

    Returns:
      True if the matrices are equivalent,
      False otherwise.
    """
    for i in range(len(matrix1)):
        for l in range(len(matrix1[0])):
            if matrix1[i][l] != matrix2[i][l]:
                return False
            
    return True

"""
matrix1 = [[1, 0, 0],
           [0, 0, 3],
           [1, 2, 0]]
matrix2 = [[1, 0, 0],
           [0, 0, 3],
           [1, 2, 0]]
print(are_equal(matrix1, matrix2))
"""

def generate_ones_matrix(rows, cols):
    """
    Create an rows by cols matrix where every
    entry is a 1.

    Inputs:
      rows - integer indicating the number of
             rows in the desired matrix
      cols - integer indicating the number of
             columns in the desired matrix

    Returns:
      A numeric matrix of the requested dimensions
      containing all 1s.
    """
    matrix = []
    for i in range(rows):
        temp = []
        matrix.append(temp)
        for l in range(cols):
            matrix[i].append(1)
    
    return matrix

"""
print(generate_ones_matrix(2,2))
"""

def is_symmetric(matrix):
    """
    Check if the matrix is symmetric.

    Inputs:
      matrix - a numeric matrix

    Returns:
      True if matrix is symmetric, False otherwise.
    """
    matrix = numeric.Matrix(matrix)
    return matrix == matrix.transpose()

"""
matrix = [[1, 1, -1],
           [1, 0, 2],
           [-1, 2, 5]]
print(is_symmetric(matrix))
"""

def check_commute(matrix1, matrix2):
    """
    Check if two matrices commute, meaning that
    the answer is the same if they are multiplied
    with each other in either order.

    Inputs:
      matrix1 - a numeric matrix
      matrix2 - a numeric matrix

    Returns:
      True if the matrices commute, False otherwise.
    """
    matrix1 = numeric.Matrix(matrix1)
    matrix2 = numeric.Matrix(matrix2)
    
    return matrix1 @ matrix2 == matrix2 @ matrix1

"""
matrix1 = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]
matrix2 = [[5, 4, 7],
           [-5, 2, 3],
           [1, 2, 2]]
print(check_commute(matrix1, matrix2))
"""

def check_magic_square(matrix):
    """
    Check if the matrix is a magic square.

    Inputs:
      matrix - a numeric matrix

    Returns:
      True if matrix is a magic square, False otherwise.
    """
    is_magic = True
    length = len(matrix)
    width = len(matrix[0])
    magic_num = 0
    for i in range(width):
        magic_num += matrix[0][i]

    for i in range(length):
        temp = 0
        for s in range(width):
            temp += matrix[i][s]
        if temp != magic_num:
            is_magic == False
            break
    
    for i in range(width):
        temp = 0
        for s in range(length):
            temp += matrix[s][i]
        if temp != magic_num:
            is_magic = False
            break
            
    temp = 0        
    for i in range(length):
        temp += matrix[i][i]
    if temp != magic_num:
        is_magic = False
        
    return is_magic
    
"""    
matrix1 = [[2,7,6],
          [9,5,1],
          [4,3,8]]
print(check_magic_square(matrix1))
matrix2 = [[4,9,2],
          [3,5,7],
          [8,1,6]]
print(check_magic_square(matrix2))
matrix3 = [[16,3,2,13],
           [5,10,11,8],
           [9,6,7,12],
           [4,15,14,1]]
print(check_magic_square(matrix3))
"""