def group_by(xs, key_function):
    group = {}
    for i in xs:
        key = key_function(i)
        if key not in group:
            group[key] = []
        group[key].append(i)
    return group