def get_matrix(N):
    matrix = []
    for i in range(N):
        row = list(map(int,input().split()))
        matrix.append(row)
    return matrix

def check_unique(matrix,N):
    after_sort = []
    for i in matrix:
        i.sort()
        after_sort.append(i)
    list1 = [i for i in range(1,N + 1)]
    if after_sort.count(after_sort[0]) == N and after_sort[0] == list1:
        return True
    else:
        return False
    

def main():
    N = int(input("Enter the size of matrix: "))
    matrix = get_matrix(N)
    output = check_unique(matrix,N)
    print(output)
    
main()