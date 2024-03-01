def get_matrix(row,col):
    matrix = []
    for i in range(row):
        rows = list(map(int,input().split()))
        matrix.append(rows)
    return matrix
    
def make_other_elements_zero(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i != j) and (i != len(matrix) - 1 - j):
                matrix[i][j] = 0
    return matrix

def display_matrix(matrix):
    for i in matrix:
        print(" ".join(map(str,i)))

def main():
    row,col = tuple(map(int,input().split()))
    matrix = get_matrix(row,col)
    diagonal_not_zero_matrix = make_other_elements_zero(matrix)
    display_matrix(diagonal_not_zero_matrix)
main()