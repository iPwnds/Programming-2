# Write your code here

import re

def equals_a(string):
    return bool(re.fullmatch('a', string))