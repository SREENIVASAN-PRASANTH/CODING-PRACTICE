def get_matrix(row,col):
    matrix = []
    for i in range(row):
        rows = list(map(int,input().split()))
        matrix.append(rows)
    return matrix
def add_zeroes(matrix):
    after_zero_added = []
    for i in matrix:
        a = [0] + i + [0]
        after_zero_added.append(a)
    after_zero_added = [[0 for i in range(len(matrix[0]) + 2)]] + after_zero_added + [[0 for i in range(len(matrix[0]) + 2)]]
    return after_zero_added
    
def convert_zero_to_sum(after_zero_added,matrix):
    for i in range(1,len(after_zero_added)-1):
        for j in range(1,len(after_zero_added[0])-1):
            if after_zero_added[i][j] == 0:
                left = after_zero_added[i][j-1]
                top = after_zero_added[i-1][j]
                bottom = after_zero_added[i + 1][j]
                right = after_zero_added[i][j + 1]
                total = left + top + bottom + right
                after_zero_added[i][j] = total
                
    return after_zero_added
    
def convert_number_to_zero(convert_zero_to_total,matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][j] = convert_zero_to_total[i + 1][j + 1]
                convert_zero_to_total[(i + 1) - 1][(j + 1)] = 0
                convert_zero_to_total[(i + 1) + 1][(j + 1)] = 0
                convert_zero_to_total[(i + 1)][(j + 1) - 1] = 0
                convert_zero_to_total[(i + 1)][(j + 1) + 1] = 0
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            matrix[i][j] = convert_zero_to_total[i + 1][j + 1]
    return matrix
    
def display_matrix(matrix):
    for i in matrix:
        print(" ".join(map(str,i)))

def main():
    row,col = map(int,input().split())
    matrix = get_matrix(row,col)
    after_zero_added = add_zeroes(matrix)
    convert_zero_to_total = convert_zero_to_sum(after_zero_added,matrix)
    converted_number_to_zero = convert_number_to_zero(convert_zero_to_total,matrix)
    display_matrix(converted_number_to_zero)
    
    
main()