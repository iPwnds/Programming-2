# Write your code here

import re

def is_valid_password(string):
    # At least 12 characters
    if len(string) < 12:
        return False
    # At least one digit
    if not re.search(r'\d', string):
        return False
    # At least one lowercase letter
    if not re.search(r'[a-z]', string):
        return False
    # At least one uppercase letter
    if not re.search(r'[A-Z]', string):
        return False
    # At least one special character from +-*/.@ 
    if not re.search(r'[+\-*/.@]', string):
        return False
    # No three times the same character in a row
    if re.search(r'(.)\1\1', string):
        return False
    # No four times the same character anywhere
    for ch in set(string):
        if string.count(ch) >= 4:
            return False
    return True