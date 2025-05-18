# Write your code here

import re

def only_vowels(string):
    return bool(re.fullmatch('(a|e|i|o|u)*', string))