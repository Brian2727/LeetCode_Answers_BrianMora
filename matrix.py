

def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    dynamic programing
    """
    arrOfZeros = [0 for x in range(len(matrix[0]))]
    matrix_copy = []
    matrix_copy.extends(matrix)
    yToZero = {}
    xToZero = {}
    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            if col == 0:
                matrix_copy[y] = arrOfZeros.copy()
                for m in range(len(matrix_copy)):
                    matrix_copy[m][x] = 0
    matrix = matrix_copy
    return matrix_copy

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setZeroes(matrix))