class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def remove(self, key):
        if not self.head:
            return

        if self.head.data == key:
            current = self.head
            while current.next != self.head:
                current = current.next
            if self.head == self.head.next:
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
                if current.data == key:
                    prev.next = current.next
                    break

    def reverse(self):
        if not self.head:
            return

        prev = None
        current = self.head
        next_node = None

        while current.next != self.head:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        current.next = prev
        self.head.next = current
        self.head = current

    def display(self):
        if not self.head:
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()

# Пример использования:
circular_list = CircularLinkedList()
circular_list.append(1)
circular_list.append(2)
circular_list.append(3)

print("Исходный замкнутый список:")
circular_list.display()

circular_list.reverse()

print("Развёрнутый замкнутый список:")
circular_list.display()
