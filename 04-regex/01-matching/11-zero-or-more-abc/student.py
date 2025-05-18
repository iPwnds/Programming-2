# Write your code here

import re

def zero_or_more_abc(string):
    return bool(re.fullmatch("(abc){0,}", string))