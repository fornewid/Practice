def to_pothole_case(s):
    return ''.join(map(lambda x: '_' + x.lower() if x.isupper() or x.isdigit() else x, s)).lstrip('_')
