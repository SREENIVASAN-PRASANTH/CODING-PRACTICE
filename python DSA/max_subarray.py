List = list(map(int,input("Enter the Array: ").split()))

def max_subarray(arr):
    max_ending_here = max_so_far = arr[0]
    start = end = temp_start = 0
    
    for i in range(1,len(arr)):
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            temp_start = i
        else:
            max_ending_here += arr[i]
            
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = i
    return arr[start:end + 1]

output = max_subarray(List)
output = ' '.join(map(str,output))
print("The maximum contiguous subarray is: ",output)