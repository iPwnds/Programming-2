def reverse_from_left(text):
    if text == "":
        return ""

    return reverse_from_left(text[1:]) + text[0]

def reverse_from_right(text):
    if text == "":
        return ""

    return text[-1] + reverse_from_right(text[:-1])
