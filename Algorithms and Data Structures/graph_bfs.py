from collections import deque

graph = {'Максим': ['Алиса', 'Арина', 'Даниил'],
         'Даниил': ['Надежда', 'Наталья', 'Алиса'],
         'Сергей': ['Зоя', 'Зинаида', 'Зухра'],
         'Алиса': ['Надежда', 'Зухра', 'Настя'],
         'Настя': ['боба', 'биба']}


def is_target(name: str) -> bool:
    """
    Функция для теста, чтобы найти цель по параметру
    :param name:
    :return:
    """
    if len(name) == 4:
        return True


def search(start_point):
    queue = deque()
    queue += (graph[start_point])
    searched = []
    iteration = 1
    while queue:
        print(f'Итерация {iteration}')
        print(f'Текущая очередь: {list(queue)}')
        element = queue.popleft()
        if element not in searched:
            print(f'Текущая проверка: {element}')
        else:
            print('Проверка не производится')
        print(f'Список проверенных: {searched}')
        print('---------------')
        if element not in searched:
            if is_target(element):
                return element
            else:
                searched.append(element)
                if element in graph.keys():
                    queue += graph.get(element)
        iteration += 1
    return None


print(search('Максим'))
