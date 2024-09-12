import numpy as np

#Matrix generation
def create_matrix(min_rand_val, max_rand_val, rows, cols):
    return np.random.randint(min_rand_val, max_rand_val, size=(rows, cols))

#matrix multiplication
def multiply(matrix_a, matrix_b):
    return np.matmul(matrix_a, matrix_b)

matrix_a = create_matrix(-1000, 1001, 20, 20)
matrix_b = create_matrix(-1000, 1001, 20, 20)
    
#print result
print('First matrix: \n', matrix_a)
print('Second matrix: \n', matrix_b)
print('Multiplication: \n', multiply(matrix_a, matrix_b))
