# ID решения 69843955
def broken_search(array, search_value):
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = start + (end-start) // 2
        guess = array[middle]
        if search_value == guess:
            return middle
        if search_value < guess:
            end = middle - 1
        else:
            start = middle + 1
    return -1

