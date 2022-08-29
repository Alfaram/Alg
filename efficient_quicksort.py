def partition(players, start, end):
    pivot = (players[start])
    i = start + 1
    j = end - 1
    while True:
        if i <= j and players[j] > pivot:
            j -= 1
        elif i <= j and players[i] < pivot:
            i += 1
        elif (players[j] > pivot) or (players[i] < pivot):
            continue
        if i <= j:
            players[i], players[j] = players[j], players[i]
        else:
            players[start], players[j] = players[j], players[start]
            return j


def quick_sort(players, start, end):
    if end - start > 1:
        p = partition(players, start, end)
        quick_sort(players, start, p)
        quick_sort(players, p + 1, end)


def transformation(players):
    players[1] = - int(players[1])
    players[2] = int(players[2])
    return [players[1], players[2], players[0]]


if __name__ == '__main__':
    number = int(input())
    competitors = [transformation(input().split()) for _ in range(number)]
    left = 0
    quick_sort(competitors, left, len(competitors))
    print(*(list(zip(*competitors))[2]), sep="\n")
