# ID решения 69916244
import random


def quicksort(array, low, high):
    if low >= high:
        return -1

    left, right = low, high
    pivot = array[random.randint(low, high)]

    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    quicksort(array, low=low, high=right)
    quicksort(array, low=left, high=high)


if __name__ == '__main__':
    n = int(input())
    users = []
    for _ in range(n):
        username, solved, errors = input().split()
        users.append([-int(solved), int(errors), username])

    quicksort(users, 0, len(users) - 1)
    for _, _, person in users:
        print(person)
