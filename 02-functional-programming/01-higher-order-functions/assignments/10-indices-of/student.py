def indices_of(xs, condition):
    indices = []
    for index, item in enumerate(xs):
        if condition(item):
            indices.append(index)
    return indices

def is_palindrome(string):
    return string == string[::-1]