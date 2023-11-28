def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Построение max-heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи в порядке убывания.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Перемещаем текущий корень в конец.
        heapify(arr, i, 0)  # Вызываем heapify для уменьшенной кучи.

arr = [12, 11, 13, 5, 6, 7]
print(f'Не отсортированный массив: {arr}')
heap_sort(arr)
print("Отсортированный массив:", arr)
