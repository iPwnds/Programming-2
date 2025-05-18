# Write your code here

import re

def equals_b(string):
    return bool(re.fullmatch('b', string))