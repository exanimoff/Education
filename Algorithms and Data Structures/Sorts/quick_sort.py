from random import *

arr = []
for i in range(15):
    arr.append(randint(1, 100))
print(arr)


def q_sort(arr):
    if len(arr) < 2:
        return arr
    pivot_index = randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    less = [i for i in arr if i < pivot]
    more = [j for j in arr if j > pivot]
    equal = [k for k in arr if k == pivot]
    return q_sort(less) + equal + q_sort(more)


print(q_sort(arr))
