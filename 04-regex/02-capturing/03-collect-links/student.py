# Write your code here

import re

def collect_links(string):
    return re.findall(r'<a\s+href="([^"]*)">', string)