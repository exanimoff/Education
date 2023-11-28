class Deque:
    def __init__(self):
        self.items = []

    def print_deque(self):
        print("Deque:", self.items)

    def is_empty(self):
        return len(self.items) == 0

    def add_left(self, item):
        self.items.insert(0, item)

    def left(self):
        return self.items[0]

    def right(self):
        return self.items[-1]

    def add_right(self, item):
        self.items.append(item)

    def remove_left(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Deque is empty")

    def remove_right(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Deque is empty")

    def size(self):
        return len(self.items)

deque = Deque()
deque.add_left(1)
deque.print_deque()
deque.add_right(2)
deque.print_deque()
deque.add_left(3)
deque.print_deque()
deque.add_left(3)
deque.print_deque()
deque.add_left(3)
deque.print_deque()
deque.add_right(5)
deque.remove_left()
deque.print_deque()
print(f'Размер дека: {deque.size()}')
print(deque.is_empty())
deque.print_deque()
print(deque.left())
print(deque.right())