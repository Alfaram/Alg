def broken_search(array: list, search_value: int) -> int:
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = start + (end-start) // 2
        if search_value == array[middle]:
            return middle
        if array[start] <= array[middle]:
            if array[start] <= search_value < array[middle]:
                end = middle - 1
            else:
                start = middle + 1
        else:
            if array[middle] < search_value <= array[end]:
                start = middle + 1
            else:
                end = middle - 1
    return -1
