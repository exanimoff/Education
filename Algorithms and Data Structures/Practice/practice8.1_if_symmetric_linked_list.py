class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def is_symmetric(lst):
    def reverse_list(node):
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev

    def if_symmetric(list1, list2):
        while list1 and list2:
            if list1.value != list2.value:
                return False
            list1 = list1.next
            list2 = list2.next
        return True

    slow = lst
    fast = lst
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    reversed_half = reverse_list(slow)

    return if_symmetric(lst, reversed_half)


lst = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
result = is_symmetric(lst)
print(result)

lst = ListNode(1, ListNode(2, ListNode(3)))
result = is_symmetric(lst)
print(result)
