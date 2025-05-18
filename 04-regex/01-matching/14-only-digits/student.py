# Write your code here

import re

def only_digits(string):
    return bool(re.fullmatch('[0123456789]*', string))