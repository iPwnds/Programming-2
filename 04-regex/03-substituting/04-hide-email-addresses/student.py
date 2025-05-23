# Write your code here

import re

def hide_email_addresses(string):
    def replace(match):
        email = match.group(0)
        return '*' * len(email)

    return re.sub(r'\b[a-z0-9.]+@[a-z0-9]+(?:\.[a-z0-9]+)+\b', replace, string, flags=re.IGNORECASE)