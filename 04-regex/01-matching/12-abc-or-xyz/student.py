# Write your code here

import re

def abc_or_xyz(string):
    return bool(re.fullmatch("abc|xyz", string))