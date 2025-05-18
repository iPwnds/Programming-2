# Write your code here

import re

def three_to_ten_times_abc(string):
    return bool(re.fullmatch("(abc){3,10}", string))