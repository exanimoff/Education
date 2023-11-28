class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def delete(self, value_to_delete):
        if not self.head:
            return

        if self.head.value == value_to_delete:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value_to_delete:
                current.next = current.next.next
                return
            current = current.next

    def search(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False

    def value_from_index(self, n):
        current = self.head
        count = 0

        while current:
            if count == n:
                return current.value
            count += 1
            current = current.next

        raise IndexError("Индекс находится за пределами размера связного списка")


# Создаем связный список и добавляем элементы
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(7)
linked_list.append(15)

# Выводим связный список
linked_list.display()

# Удаляем элемент со значением 3
linked_list.delete(3)

# Выводим обновленный связный список
linked_list.display()

# Ищем элемент со значением 3
num = 5
if linked_list.search(num):
    print(f"Элемент {num} найден в связном списке.")
else:
    print(f"Элемент {num} не найден в связном списке.")

# Получаем значение 2-го элемента (нумерация начинается с 0)
n = 2
value = linked_list.value_from_index(n)
print(f"Значение {n}-го индекса: {value}")
