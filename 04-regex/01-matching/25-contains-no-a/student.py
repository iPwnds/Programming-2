# Write your code here

import re

def contains_no_a(string):
    return bool(re.fullmatch(r'[^a]*', string))