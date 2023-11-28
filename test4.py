def min_completion_time(tasks, k):
    """
    Сложность O(N*logN), с использованием сортировки по убыванию
    :param tasks:
    :param k:
    :return:
    """
    sorted_tasks = sorted(tasks, reverse=True)
    completion_times = [0] * k

    for task_time in sorted_tasks:
        min_index = completion_times.index(min(completion_times))

        completion_times[min_index] += task_time


        print(f"Задача с весом {task_time} обработана процессором {min_index + 1}")
        print(f"Текущее состояние процессоров: {completion_times}")

    return max(completion_times)


tasks = [3, 7, 5, 10, 8]
k = 3
result = min_completion_time(tasks, k)
print(f"Минимальное время завершения: {result}")

