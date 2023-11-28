char_list = []
a = []

for char in input().split():
    if not a:
        a.append(char)
    else:
        if a[-1] == char:
            a.append(char)
        else:
            char_list.append(a.copy())
            a.clear()
            a.append(char)

char_list.append(a.copy())  # добавляем последний непустой список 'a'

print(char_list)
