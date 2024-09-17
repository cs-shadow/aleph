import numpy as np
def multiply(matrix_a, matrix_b):
    result = np.dot(matrix_a, matrix_b)
    return result

def generate_random_matrix(n, m):
    matrix_x = matrix_a= np.random.randint(1, high=1000, size=(n,m), dtype='l')
    return matrix_x

n=20
m=20

matrix_a= generate_random_matrix(n,m)
print("Matrix A")
print(matrix_a)
print("\n")


matrix_b= generate_random_matrix(n,m)
print("Matrix B")
print(matrix_b)
print("\n")

result = multiply(matrix_a, matrix_b)
print("matrix_a . matrix_b = ")
print(result)