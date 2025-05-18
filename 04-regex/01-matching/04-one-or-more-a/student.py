# Write your code here

import res

def one_or_more_a(string):
    return bool(re.fullmatch("a+", string))