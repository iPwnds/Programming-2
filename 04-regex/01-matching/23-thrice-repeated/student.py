# Write your code here

import re

def thrice_repeated(string):
    return bool(re.fullmatch(r'(.+)\1\1', string))