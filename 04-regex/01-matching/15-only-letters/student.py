# Write your code here

import re

def only_letters(string):
    return bool(re.fullmatch('[a-z|A-Z]*', string))