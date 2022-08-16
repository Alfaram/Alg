# ID решения 69583401

from collections import Counter


def count_point(number_buttons, array, people=2, aggregate='.'):
    return sum(
        count <= people * number_buttons
        for key, count in Counter(array).items()
        if key != aggregate
    )


if __name__ == '__main__':
    print(
        count_point(
            int(input()),
            f'{input()}{input()}{input()}{input()}'
        )
    )
