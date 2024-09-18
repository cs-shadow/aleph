import numpy as np

def multiply(A, B):
    C = np.zeros([20, 20], dtype = 'l')
    #"""
    for i in range (len(A)):
        for j in range (len(B)):
            for k in range (len(B)):
                C[i][j] += A[i][k]*B[k][j]
    #"""
    #OR using Matmul
    #C = np.matmul(A,B)
    return C
# Generate two matrices based on random numbers
matrix_a = np.random.randint(0, 1000, size=(20, 20), dtype='l')
matrix_b = np.random.randint(0, 1000, size=(20, 20), dtype='l')

# Multiply the matrices and print the result
result = multiply(matrix_a, matrix_b )
print("A: ")
print(matrix_a)
print("B: ")
print(matrix_a)
print("AxB= ")
print(result)
