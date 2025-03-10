import pytest
import student


def closest(points, target_point):
    def distance(point):
        x, y = point
        dx = x - tx
        dy = y - ty
        return dx**2 + dy**2

    tx, ty = target_point
    return min(points, key=distance)

@pytest.mark.skipif('closest' not in dir(student), reason='closest not ')
@pytest.mark.parametrize("points", [
    [(0, 0)],
    [(8, 0), (0, 8)],
    [(1, 4), (2, 3), (4, 7), (9, 1), (5, 5)],
])
@pytest.mark.parametrize("target_point", [
    (x, y)
    for x in range(0, 11)
    for y in range(0, 11)
])
def test_closest(points, target_point):
    expected = closest(points, target_point)
    actual = student.closest(points, target_point)

    assert expected == actual
