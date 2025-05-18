# Write your code here

import re

def ten_times_abc(string):
    return bool(re.fullmatch("(abc){10}", string))