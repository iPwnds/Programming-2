# Write your code here

import re

def equals_abc(string):
    return bool(re.fullmatch('abc', string))