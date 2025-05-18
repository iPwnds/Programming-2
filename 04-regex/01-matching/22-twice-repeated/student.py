# Write your code here

import re

def twice_repeated(string):
    return bool(re.fullmatch(r'(.)\1', string))