# ID решения 69718431
from operator import add, sub, mul, floordiv


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError('Стек пуст.')


OPERATORS = {'+': add,
             '-': sub,
             '*': mul,
             '/': floordiv}


def postfix_notation(lines, stack=None, converter=int, operators=OPERATORS):
    stack = Stack() if stack is None else stack
    for element in lines:
        if element in operators:
            element_1, element_2 = stack.pop(), stack.pop()
            stack.push(operators[element](element_2, element_1))
        else:
            try:
                stack.push(converter(element))
            except ValueError:
                raise ValueError(
                    f'Невозможно преобразовать "{element}" '
                    f'в {converter.__name__} или неподдерживаемая операция.')
    return stack.pop()


if __name__ == '__main__':
    print(postfix_notation(input().split()))
