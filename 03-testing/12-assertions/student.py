def is_sorted(lst):
    """Check if the list is sorted in non-decreasing order."""
    return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))

def split_in_two(ns):
    assert isinstance(ns, list), "Input must be a list"
    middle = len(ns) // 2
    left = ns[:middle]
    right = ns[middle:]
    # The split should reconstruct the original list when concatenated
    assert left + right == ns, "Split lists must concatenate to original"
    return (left, right)

def merge_sorted(ks, ns):
    assert is_sorted(ks), "First input to merge must be sorted"
    assert is_sorted(ns), "Second input to merge must be sorted"

    result = []
    i = 0
    j = 0
    while i < len(ks) and j < len(ns):
        if ks[i] < ns[j]:
            result.append(ks[i])
            i += 1
        else:
            result.append(ns[j])
            j += 1

    result.extend(ks[i:])
    result.extend(ns[j:])

    # Check that the merged list is sorted
    assert is_sorted(result), "Merged result must be sorted"
    # The length of the merged list must equal sum of input lengths
    assert len(result) == len(ks) + len(ns), "Merged result must have combined length"
    return result

def merge_sort(ns):
    assert isinstance(ns, list), "Input must be a list"

    if len(ns) <= 1:
        result = ns
    else:
        left, right = split_in_two(ns)
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        result = merge_sorted(sorted_left, sorted_right)

    # Final result must be sorted and same length as input
    assert is_sorted(result), "Result of merge_sort must be sorted"
    assert len(result) == len(ns), "Result length must equal input length"
    return result