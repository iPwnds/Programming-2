def merge_dictionaries(d1, d2, merge_function):
    merged = {}

    # Add all keys and values from d1
    for key, value in d1.items():
        merged[key] = value

    # Add or merge values from d2
    for key, value in d2.items():
        if key in merged:
            merged[key] = merge_function(merged[key], value)
        else:
            merged[key] = value

    return merged