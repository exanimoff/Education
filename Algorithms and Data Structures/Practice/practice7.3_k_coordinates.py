from math import sqrt

lst = [[5, 5], [6, 6], [3, 4], [7, 7], [2, 3]]
start = [0, 0]
k = 2
point_distances = []

for point in lst:
    distance = sqrt(point[0] ** 2 + point[1] ** 2)
    point_distances.append((distance, point))

point_distances.sort()

nearest_points = [point for distance, point in point_distances[:k]]
print(f'Дистанции: {point_distances}')
print("Ближайшие", k, "точки к началу координат:")
for point in nearest_points:
    print(point)
