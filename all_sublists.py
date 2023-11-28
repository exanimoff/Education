subs = [[]]
lst = input().split()
n = len(lst)
for rotate in range(len(lst)):
    index = rotate + 1
    for i in range(n):
        subs.append(lst[i:i + index])
    n -= 1
print(subs)