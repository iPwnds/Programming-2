def rle_encode(data):
    # Convert the data to an iterator if it isn't one already
    data_iter = iter(data)

    try:
        # Start by getting the first character
        current_char = next(data_iter)
        count = 1

        for char in data_iter:
            if char == current_char:
                count += 1  # Increment count for the same character
            else:
                # Yield the current character and count, then reset for the next character
                yield (current_char, count)
                current_char = char
                count = 1

        # Yield the last group of characters
        yield (current_char, count)

    except StopIteration:
        # In case the input is empty, just return
        pass


def rle_decode(data):
    for char, count in data:
        for _ in range(count):
            yield char