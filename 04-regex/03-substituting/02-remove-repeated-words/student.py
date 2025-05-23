# Write your code here

import re

def remove_repeated_words(string):
    pattern = r'\b(\w+)\b\s+\1\b'
    while re.search(pattern, string, flags=re.IGNORECASE):
        string = re.sub(pattern, r'\1', string, flags=re.IGNORECASE)
    return string