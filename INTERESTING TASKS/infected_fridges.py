n = int(input())
data = [input() for i in range(n)]
infected_fridges = []
word = 'anton'
for i in range(n):
    found_all_chars = True
    for char in word:
        if char in data[i]:
            index = data[i].find(char)
            data[i] = data[i][index:]
        elif char not in data[i]:
            found_all_chars = False
            break
    if found_all_chars:
        infected_fridges.append(i + 1)
print(*infected_fridges)