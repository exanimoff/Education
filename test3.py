import heapq

def min_completion_time(tasks, k):
    """
    Сложность O(N*logK), без сортировки списка задач.
    Благодаря использованию кучи мы не тратим лишнее время на определение наименее загруженного потока
    :param tasks:
    :param k:
    :return:
    """
    processors = [0] * k

    heap = [(0, i) for i in range(k)]
    heapq.heapify(heap)

    for task_time in tasks:
        current_time, processor = heapq.heappop(heap)

        current_time += task_time
        processors[processor] = current_time

        heapq.heappush(heap, (current_time, processor))
        print(f"Задача с весом {task_time} обработана процессором {processor + 1}")
        print(f"Текущее состояние процессоров: {processors}")

    return max(processors)

tasks = [3, 7, 5, 10, 8]
k = 3
result = min_completion_time(tasks, k)
print(f"Минимальное время завершения: {result}")
