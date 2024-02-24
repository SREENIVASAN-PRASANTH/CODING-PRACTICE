List = list(map(int,input("Enter the Array: ").split()))

def max_subarray(arr):
    current_max = max = arr[0]
    start = end = temp_start = 0
    
    for i in range(1,len(arr)):
        if arr[i] > current_max + arr[i]:
            current_max = arr[i]
            temp_start = i
        else:
            current_max += arr[i]
            
        if current_max > max:
            max = current_max
            start = temp_start
            end = i
    return arr[start:end + 1]

output = max_subarray(List)
output = ' '.join(map(str,output))
print("The maximum contiguous subarray is: ",output)