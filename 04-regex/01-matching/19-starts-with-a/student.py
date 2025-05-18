# Write your code here

import re

def starts_with_a(string):
    return bool(re.match('a', string))