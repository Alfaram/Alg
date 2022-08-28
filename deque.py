# ID решения 69719024
class Deque:
    def __init__(self, max_size: int):
        self._elements = [None] * max_size
        self._max_size = max_size
        self._head = 1
        self._tail = 0
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._max_size

    def push_back(self, value: int):
        if self.is_full():
            raise IndexError('Дек переполнен')
        self._tail = (self._tail + 1) % self._max_size
        self._elements[self._tail] = value
        self._size += 1

    def push_front(self, value: int):
        if self.is_full():
            raise IndexError('Дек переполнен')
        front_head = self._head - 1
        self._head = front_head % self._max_size
        self._elements[front_head] = value
        self._size += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError('Дек пуст')
        value = self._elements[self._tail]
        back_tail = self._tail - 1
        self._tail = back_tail % self._max_size
        self._size -= 1
        return value

    def pop_front(self):
        if self.is_empty():
            raise IndexError('Дек пуст')
        value = self._elements[self._head]
        self._head = (self._head + 1) % self._max_size
        self._size -= 1
        return value


if __name__ == '__main__':
    count_command = int(input())
    queue = Deque(int(input()))
    for _ in range(count_command):
        operation, *values = input().split()
        try:
            result = getattr(queue, operation)(*values)
            if result is not None:
                print(result)
        except AttributeError:
            raise ValueError(f'Неожиданная команда {operation}!')
        except IndexError:
            print('error')
