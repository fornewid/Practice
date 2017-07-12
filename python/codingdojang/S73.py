import re
def zip_by_char(s):
    return ''.join('%s%d' % (cs.group(0)[0], len(cs.group(0))) for cs in re.finditer(r'(\w)\1*', s))
