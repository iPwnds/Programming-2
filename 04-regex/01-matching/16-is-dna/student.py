# Write your code here

import re

def is_dna(string):
    return bool(re.fullmatch('[GATC]*', string))