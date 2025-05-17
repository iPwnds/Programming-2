def split_in_two(ns):
    mid = len(ns) // 2
    return ns[:mid], ns[mid:]

def merge_sorted(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append remaining elements (only one of these two will have elements)
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(ns):
    if len(ns) <= 1:
        return ns[:]
    left, right = split_in_two(ns)
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge_sorted(sorted_left, sorted_right)