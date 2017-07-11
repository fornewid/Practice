import re
def replace_even_number(s):
    repl=lambda m: m.group(1) + (m.group(2) if m.group(2) else '*')
    return re.sub(r'(.)(?:\d|(\D))', repl, s)

# test_str = 'a1b2cde3~g45hi6'
# print(replace_even_number(test_str))
# print('a*b*cde*~g4*hi6')
# print(replace_even_number(test_str) == 'a*b*cde*~g4*hi6')

# def replace_even_number(s):
#     new_s = ''
#     for i in range(0, len(s)):
#         if i % 2 is not 0 and s[i].isdigit():
#             new_s += '*'
#         else:
#             new_s += s[i]
#     return new_s