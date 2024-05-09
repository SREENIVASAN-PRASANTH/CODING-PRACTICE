def binary_search(array,element):
    low = 0
    high = len(array) - 1
    middle = None
    
    if len(array) % 2 == 0:
        middle = len(array) // 2
    else:
        (len(array) // 2) + 1
    
    while (low <= high):
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            high = middle - 1
        else:
            low = middle + 1