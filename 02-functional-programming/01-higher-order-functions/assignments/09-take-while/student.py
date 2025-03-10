def take_while(xs, condition):
    first_list = []
    second_list = []

    for x in xs:
        if condition(x):
            first_list.append(x)
        else:
            second_list = xs[xs.index(x):]  # Add the remaining elements
            break

    return (first_list, second_list)