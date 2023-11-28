class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_duplicates(self):
        current = self.head

        while current:
            data = current.data

            runner = current.next
            while runner:
                if runner.data == data:
                    if runner.next:
                        runner.next.prev = runner.prev
                    runner.prev.next = runner.next
                runner = runner.next

            current = current.next

    def print_dll(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(2)
dll.append(5)
dll.append(3)

print("Исходный двусвязный список:")
dll.print_dll()
dll.remove_duplicates()

print("Двусвязный список после удаления дубликатов:")
dll.print_dll()