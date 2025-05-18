# Write your code here

import re

def ten_or_more_abc(string):
    return bool(re.fullmatch("(abc){10,}", string))