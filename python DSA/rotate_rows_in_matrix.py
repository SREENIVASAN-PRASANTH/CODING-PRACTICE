def get_matrix(N):
    matrix = []
    for i in range(N):
        row = list(map(int,input().split()))
        matrix.append(row)
    return matrix
    
def rotate_matrix(rotation,matrix):
    rotated_matrix = []
    for i in matrix:
        i = i[rotation:] + i[:rotation]
        rotated_matrix.append(i)
    for i in rotated_matrix:
        print(" ".join(map(str,i)))
    
def main():
    N = int(input())
    matrix = get_matrix(N)
    rotation = int(input())
    if rotation > len(matrix) and 1 <= rotation <= 10:
        print("Shifting not possible")
    else:
        rotate_matrix(rotation,matrix)
        
main()