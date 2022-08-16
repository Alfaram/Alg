class Queue:
    def __init__(self, max_capacity):
        self.queue = [None] * max_capacity
        self.max_capacity = max_capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, value):
        if self.size != self.max_capacity:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_capacity
            self.size += 1
        else:
            raise OverflowError

    def push_front(self, value):
        if self.size != self.max_capacity:
            self.queue[self.head - 1] = value
            self.head = (self.head - 1) % self.max_capacity
            self.size += 1
        else:
            raise OverflowError

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        value = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_capacity
        self.size -= 1
        return value

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_capacity
        self.size -= 1
        return value


def main():
    count_command = int(input())
    queue_size = int(input())
    queue = Queue(queue_size)
    methods = {
        'push_front': queue.push_front,
        'push_back': queue.push_back,
        'pop_front': queue.pop_front,
        'pop_back': queue.pop_back,
    }
    for i in range(count_command):
        command = input()
        operation, *value = command.split()
        if value:
            try:
                methods[operation](int(*value))
            except OverflowError:
                print('error')
        else:
            try:
                result = methods[operation]()
                print(result)
            except IndexError:
                print('error')


if __name__ == '__main__':
    main()
