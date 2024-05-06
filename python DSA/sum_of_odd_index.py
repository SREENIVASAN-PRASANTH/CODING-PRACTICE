N = [1,2,3,4]
sum_odd_index = 0
for i in N:
    if N.index(i) % 2 != 0:
        sum_odd_index = sum_odd_index + N.index(i)

print(sum_odd_index)