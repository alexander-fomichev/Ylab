from itertools import permutations

def dist(point_1, point_2):
    """
    принимает координаты двух точек, возвращает расстояние между ними
    """
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


# исходные точки маршрута
points = ((0, 2), (2, 5), (5, 2), (6, 6), (8, 3))
# матрица смежности
distances = tuple(tuple(dist(x, y) for x in points) for y in points)

# for x in distances:
#     print(*x)


min_lenght = 0

for route in permutations(range(1, 5)):
    current_point = 0
    current_lenght = 0
    current_route = f"{points[0]} "
    for next_point in route:
        if min_lenght and current_lenght >= min_lenght:
            break
        current_lenght += distances[current_point][next_point]
        current_point = next_point
        current_route += f"-> {points[current_point]}[{current_lenght}] "
    current_lenght += distances[current_point][0]

    if not min_lenght or (min_lenght and min_lenght > current_lenght):
        min_lenght = current_lenght
        current_route += f"-> {points[0]}[{current_lenght}] = [{current_lenght}]"
        min_route = current_route

print(min_route)


