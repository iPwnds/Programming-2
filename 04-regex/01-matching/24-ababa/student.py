# Write your code here

import re

def ababa(string):
    return bool(re.match(r'^(.+?)(.+?)\1\2\1$', string))