<<<<<<< HEAD
def closest(points, target_points):
    return min(points, key=lambda point: ((point[0] - target_points[0]) ** 2) + ((point[1] - target_points[1]) ** 2))
=======
<<<<<<< HEAD
def closest(points, target_points):
    return min(points, key=lambda point: ((point[0] - target_points[0]) ** 2) + ((point[1] - target_points[1]) ** 2))
=======
def closest(points, target_point):
    
    def distance(p1, p2):
        return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)**0.5

    closest_point = points[0]
    min_distance = distance(closest_point, target_point)

    for point in points[1:]:
        dist = distance(point, target_point)
        if dist < min_distance:
            closest_point = point
            min_distance = dist

    return closest_point
>>>>>>> 4c5538f (lambdas done)
>>>>>>> ed8a254985fdbea0724333353397ffdce5e6b793
