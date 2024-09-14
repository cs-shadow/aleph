# TODO: Implement this
import numpy as np
def multiply(matrix_a, matrix_b):
    result = np.dot(matrix_a, matrix_b)
    return result

# Generate two matrices based on random numbers
# HINT: you can use something like `random.randint(1, 1000)`
# TODO: Implement this
matrix_a = np.random.randint(1, high=1000, size=(2,2), dtype='l')
print("Matrix A = ", matrix_a)
matrix_b = np.random.randint(1, high=1000, size=(2,2), dtype='l')
print("Matrix B = ", matrix_b)

# Multiply the matrices and print the result
result = multiply(matrix_a, matrix_b)

# TODO: Write code to print the result on screen
print("Result = ", result)
