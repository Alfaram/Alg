# ID решения 69576717

from collections import Counter


def count_point(number_buttons, array, people=2, aggregate='.'):
    c = Counter(array)
    print(c)
    a = [x for key, x in c.items() if key != aggregate]
    print(a)


if __name__ == '__main__':
    number_buttons = 3
    array = '12312..22..22..2'
    print(count_point(number_buttons, array))
