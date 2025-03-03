def find(items, condition):
    for item in items:
        if condition(item):
            return item
    return None