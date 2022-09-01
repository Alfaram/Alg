def find_pivot(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= arr[high]:
            low = mid + 1
        else:
            high = mid
    return high if high else len(arr) - 1


print(find_pivot([5, 1]))
