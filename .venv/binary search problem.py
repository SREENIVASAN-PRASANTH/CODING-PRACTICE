def get_peak_element(arr):
    # #getting max element
    # max_ele = arr[0]
    #
    # for i in arr:
    #     if i > max_ele:
    #         max_ele =  i

    # arr = sorted(arr)

    #binary_search
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if mid == 0:    #if the peak is at starting index
            return mid
        if mid == len(arr) - 1:     #if the peak is at ending index
            return mid

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]: #if the peak is at middle of index
            return mid
        elif arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1
    return -1           #if the peak is not found

if __name__ == "__main__":
    N = 6
    arr = [1,2,3,5,3,2]
    peak = get_peak_element(arr)
    print(peak)