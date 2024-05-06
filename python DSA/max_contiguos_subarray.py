def max_sum(a,size):
    max_so_far = 0
    max_ending_here = 0
    for i in range(0,size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

a = [-2,-1,1,2,3]
print(max_sum(a,len(a)))