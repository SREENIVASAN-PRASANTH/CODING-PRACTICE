#getting the matrix
def get_matrix(row):
     matrix = []
     for i in range(row):
         row_elements = list(map(int,input().split()))
         matrix.append(row_elements)
     return matrix

if __name__ == "__main__":
    row = int(input("Enter the row size: "))
    matrix = get_matrix(row)
    #assigning the top botom and left right values to access the elements in the matrix
    top = 0
    bottom = len(matrix)
    left = 0
    right = len(matrix[0])
    
    '''
    
    consider a matrix
     --     --
     | 1 2 3 |
     | 4 5 6 |
     | 7 8 9 |
     --     --
     
    reduced subtraction
    
    sum of odd index in an array
    negative values in a array
    negative values in a array
     
     '''
    while (top < bottom and left < right):
        
        for i in range(left,right):
            print(matrix[top][i],end = "->") #It will iterate elements 1 -> 2 -> 3
            
        top = top + 1
        
        for i in range(top,bottom):
            print(matrix[i][right - 1],end = "->") #It  will iterate the elements 6 -> 9
            
        right = right - 1
        
        for i in range(right-1,left - 1,-1):
            print(matrix[bottom - 1][i], end = "->") #This will print 8 -> 7
        
        bottom = bottom - 1
        
        for i in range(bottom-1,top - 1,-1):
            print(matrix[i][left], end = "->") #the last iteration 4 -> 5
        
        left = left + 1
    print("None")