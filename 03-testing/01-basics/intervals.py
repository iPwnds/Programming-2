def overlapping_intervals(interval1, interval2):
    left1, right1 = interval1
    left2, right2 = interval2

    # If either interval is empty, no overlap
    if left1 > right1 or left2 > right2:
        return False

    return left1 <= right2 and left2 <= right1