def caesar(s, n):
    pre_defined = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = n % len(pre_defined)
    transform = pre_defined[n:] + pre_defined[:n]
    return ''.join([transform[pre_defined.find(_)] for _ in s])

# print(caesar('CAT', 5))
