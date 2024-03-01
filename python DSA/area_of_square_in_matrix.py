m,n = map(int,input("Enter the no.of rows and column: ").split())
s = []
for i in range(m):
    l = list(map(str,input().split()))
    s.append(l)

b = [[0 for i in range(n + 1)] for j in range(m + 1)]

area = 0

for i in range(1,len(b)):
    for j in range(1,len(b[i])):
        if s[i-1][j-1] == "X":
            b[i][j] = min(b[i-1][j-1],b[i-1][j],b[i][j-1]) + 1
            area = max(area,b[i][j])
print("The area of the big square is:",area * area)