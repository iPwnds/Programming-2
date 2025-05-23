# Write your code here

import re

def remove_trailing_whitespace(string):
    return re.sub(r'[ \t]+$', '', string, flags=re.MULTILINE)