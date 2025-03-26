import itertools

def find_shortest_path(distance, city_count):
    cities = list(range(1, city_count))

    shortest_path = None
    min_distance = float('inf')

    for perm in itertools.permutations(cities):
        path = [0] + list(perm) + [0]

        total_distance = sum(distance(path[i], path[i + 1]) for i in range(len(path) - 1))

        if total_distance < min_distance:
            min_distance = total_distance
            shortest_path = path

    return shortest_path