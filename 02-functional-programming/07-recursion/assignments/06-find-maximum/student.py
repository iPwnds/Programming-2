def findMaximum(list):
    if len(list) == 0:
        raise IndexError

    maximum = list[0]
    for i in range(len(list)):
        if list[i] > maximum:
            maximum = list[i]

    return maximum