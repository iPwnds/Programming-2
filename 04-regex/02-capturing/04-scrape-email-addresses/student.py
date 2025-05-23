# Write your code here

import re

def scrape_email_addresses(string):
    return re.findall(r'\b[a-z0-9.]+@[a-z0-9]+(?:\.[a-z0-9]+)+\b', string)