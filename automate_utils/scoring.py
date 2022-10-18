import re
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_numeric(s, pattern='[-+]?(?:\d+\.\d+|\d+)'):
    return re.findall(r'{}'.format(pattern), s)