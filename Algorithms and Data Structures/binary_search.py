lst = [x*3 for x in range(15)]
def binary_search(data, target):
    """
    :param data: iterable
    :param target: int
    :return: int
    """
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif target > data[mid]:
            left = mid + 1
        elif target < data[mid]:
            right = mid - 1
    return -1
print(lst)
print(binary_search(lst, 42))
