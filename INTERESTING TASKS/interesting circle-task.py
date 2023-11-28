n = int(input())
k = int(input())
circle = list(range(1, n+1))
index = 0
while len(circle) > 1:
    index = (index + k - 1) % len(circle)  # вычисляем индекс элемента для удаления
    print(circle, index) # вывод логов
    circle.pop(index)
last_person = circle[0]
print(last_person)
