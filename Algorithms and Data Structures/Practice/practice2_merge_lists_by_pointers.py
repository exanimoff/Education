lst1 = [1, 3, 7]
lst2 = [5, 6, 10]
k = 1
pointer1 = 0
pointer2 = 0
result = []
while pointer1 <= len(lst1) - 1 and pointer2 <= len(lst2) - 1:
    print(f'шаг {k}: pointer1 = {pointer1}, pointer2 = {pointer2}')
    k += 1
    if lst1[pointer1] < lst2[pointer2]:
        result.append(lst1[pointer1])
        pointer1 += 1
    else:
        result.append(lst2[pointer2])
        pointer2 += 1
    print(f'Результат после шага: {result}')
if pointer1 <= len(lst1) - 1:
    result.extend(lst1[pointer1:])
elif pointer2 <= len(lst2) - 1:
    result = result + lst2[pointer2:]
print(f'Итог: {result}')
