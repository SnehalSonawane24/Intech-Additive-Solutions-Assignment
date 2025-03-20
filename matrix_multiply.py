# Takes input for an n x n matrix
def get_matrix(n, name):
    
    print(f"Enter the elements of matrix {name}")
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            return get_matrix(n, name)
        matrix.append(row)
    return matrix

# Multiplies two n x n matrices
def matrix_multiply(A, B, n):
   
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Prints the matrix
def print_matrix(matrix):

    for row in matrix:
        print(" ".join(map(str, row)))

# Taking user input
n = int(input("Enter the size of matrix "))

A = get_matrix(n, "A")
B = get_matrix(n, "B")

# Performing matrix multiplication
result = matrix_multiply(A, B, n)

print("\nResultant Matrix:")
print_matrix(result)

"""
Enter the size of matrix 2
Enter the elements of matrix A
1 1
2 2
Enter the elements of matrix B
2 2
1 1

Resultant Matrix:
3 3
6 6
"""