def get_matrix(m,n):
    matrix = []
    for i in range(m):
        row = input().split()
        matrix.append(row)
    return matrix
    
def check_submatrix_having_zero(matrix,i,j,k,l):
    for m in range(0,k + 1):
        for n in range(0,l + 1):
            if (matrix[i + m][j + n] == "O"):
                return True
    return False
    
def get_max_submatrix_area(matrix,rows,columns,i,j):
    max_submatrix_area = 0
    for k in range(0,rows-i):
        for l in range(0,columns-j):
            is_submatrix_contains_zero = check_submatrix_having_zero(matrix,i,j,k,l)
            if not is_submatrix_contains_zero:
                max_submatrix_area = max(max_submatrix_area,(k + 1)*(l + 1))
    return max_submatrix_area
        
def max_area_rectangle(matrix,rows,columns):
    max_area_rectangle = 0
    for i in range(rows):
        for j in range(columns):
            if (matrix[i][j] == "X"):
                max_submatrix_area = get_max_submatrix_area(matrix,rows,columns,i,j)
                max_area_rectangle = max(max_area_rectangle,max_submatrix_area)
    return max_area_rectangle

def main():
    m,n = map(int,input("Enter the rows and column: ").split())
    matrix = get_matrix(m,n)
    output = max_area_rectangle(matrix,m,n)
    print(output)

main()