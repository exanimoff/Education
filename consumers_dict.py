consumers = {}
lst = []
for _ in range(int(input())):
    lst.append(input())
for row in lst:
    info = row.split()
    name, item, quantity = info[0], info[1], int(info[2])
    if name not in consumers:
        consumers[name] = {}
    if item in consumers[name]:
        consumers[name][item] += quantity
    else:
        consumers[name][item] = quantity
for key in sorted(consumers.keys()):
    print(f'{key}:')
    for item in sorted(consumers[key].keys()):
        print(f'{item} {consumers[key][item]}')