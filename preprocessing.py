import re

def normalize(t):
    return re.sub(r'\s+',' ',t).strip()
