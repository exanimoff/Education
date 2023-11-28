class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def reverse(self):
        current = self.head
        prev_node = None
        while current:
            current.next, current.prev = current.prev, current.next
            prev_node = current
            current = current.prev
        self.head = prev_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# Пример использования:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

print("Исходный двусвязный список:")
dll.display()

dll.reverse()

print("Развёрнутый двусвязный список:")
dll.display()
