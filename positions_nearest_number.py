# ID решения 69584594


def distance_search(array, desired_number='0'):
    length_array = len(array)
    result = [0] * length_array
    zeroes = [
        index
        for index, value in enumerate(array)
        if value == desired_number
    ]
    first = zeroes[0]
    for pos in range(first):
        result[pos] = first - pos
    for prev, next in zip(zeroes, zeroes[1:]):
        for position in range(prev + 1, next):
            result[position] = min(position - prev, next - position)
    last = zeroes[-1]
    if last != length_array - 1:
        for pos in range(last + 1, length_array):
            result[pos] = pos - last
    return result


if __name__ == '__main__':
    input()
    print(*distance_search(input().split()))
