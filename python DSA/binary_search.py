def binary_search(array,element):
    low = 0
    high = len(array) - 1
    
    while(low <= high) :
        mid = (low + high) // 2
        if array[mid] == element:
            return mid
        elif element < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
        

if __name__ == "__main__":
    a = [1,2,3,4,5]
    element_at_index = binary_search(a,7)
    print(element_at_index)