def matching_parentheses(string):
    count = 0
    for char in string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:  # closing paren before an opening one
                return False
    return count == 0