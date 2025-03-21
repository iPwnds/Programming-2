import itertools

def rle_encode(data):
    return ((key, len(list(group))) for key, group in itertools.groupby(data))

def rle_decode(data):
    for char, count in data:
        for _ in range(count):
            yield char