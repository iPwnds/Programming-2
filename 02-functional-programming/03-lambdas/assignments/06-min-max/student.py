def closest(points, target_points):
    return min(points, key=lambda point: ((point[0] - target_points[0]) ** 2) + ((point[1] - target_points[1]) ** 2))