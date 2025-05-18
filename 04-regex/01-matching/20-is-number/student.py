# Write your code here

import re

def is_number(string):
    return bool(re.fullmatch(r'\d+(\.\d+)?', string))