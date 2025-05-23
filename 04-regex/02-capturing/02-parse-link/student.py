# Write your code here

import re

def parse_link(string):
    match = re.fullmatch(r'<a\s+href="([^"]*)">(.*?)</a>', string)
    if match:
        link, caption = match.groups()
        return caption, link
    return None