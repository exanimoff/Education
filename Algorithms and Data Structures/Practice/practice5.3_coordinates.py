from math import sqrt
lst = [[5, 5], [6, 6], [3, 4]]
start = [0, 0]
min_distance = float("inf")
for point in lst:
    distance = sqrt(point[0]**2 + point[1]**2)
    if distance < min_distance:
        min_distance = distance
print(min_distance)