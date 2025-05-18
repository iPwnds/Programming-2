# Write your code here

import re

def is_valid_student_id(string):
    return bool(re.fullmatch(r'[sr]\d{7}', string, re.IGNORECASE))