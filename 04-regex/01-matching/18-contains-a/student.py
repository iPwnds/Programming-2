import re

def contains_a(string):
    return bool(re.search('a', string))