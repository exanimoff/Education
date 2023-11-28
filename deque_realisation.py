from collections import deque as dq
n, m = map(int, input().split())
matrix = []
arr = [i+1 for i in range(m)]
deque_arr = dq(arr, m)
#for num in deque_arr:
#    print(num, end=' ')
#print()
#print()
for i in range(n):
    row = deque_arr
    matrix.append(row)
    print(*row)
    deque_arr.append(row[0])

