import numeric

a = 0
b = 0


mat1 = numeric.Matrix([[4,2],
                       [1,-3]])
mat1_inv = mat1.inverse()

mat1sol = numeric.Matrix([[15],
                          [0]])

solution = mat1_inv @ mat1sol
print(solution)
print(45/14, 15/14)

mat2 = numeric.Matrix([[1,2,1],
                       [1,-2,2],
                       [0,3,2]])
                     
mat2sol = numeric.Matrix([[0],
                          [33],
                          [11]])


mat2_inv = mat2.inverse()

solution2 = mat2_inv @ mat2sol

print(solution2)
print(-3, -5, 13)
 
print("------------")

def lin_equations(var_side,sol_side):
    '''
    Objective: solve a system of linear equations represented using matrices

    Inputs: var_side: a matrix representing the side of the equations with variables, containing the coefficients of the variables, variables are identified by the index within a row
            sol_side: a matrix representing the solution side of the equation, should contain only constants, dimensions should be 1x (the number of equations in the system)
    
    Outputs: solution: a matrix representing the solution of the equation, value of variables in solution in the same order as identified in var_side

    '''
    inverse_var_side = var_side.inverse()
    solution = inverse_var_side @ sol_side
    return solution

mat4 = numeric.Matrix([[3,4,1,4,0,4],
                       [5,5,6,0,9,8],
                       [6,9,2,6,5,4],
                       [0,8,3,8,5,9],
                       [0,5,0,6,7,7],
                       [3,2,5,1,0,6]])
mat4solside = numeric.Matrix([[291],
                       [693],
                       [505],
                       [730],
                       [591],
                       [371]])

print(lin_equations(mat4,mat4solside))

