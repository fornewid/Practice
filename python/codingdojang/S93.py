def same_count(s):
    cnts = {str(i): 0 for i in range(10)}
    for c in s:
        cnts[c] += 1
    return len(set(cnts.values())) == 1

# print(True  == same_count('0123456789'))
# print(False == same_count('01234'))
# print(False == same_count('01234567890'))
# print(True  == same_count('6789012345'))
# print(False == same_count('012322456789'))

def one_count(s):
    return sorted([x for x in s]) == [str(i) for i in range(10)]

# print(one_count('0123456789'))
# print(one_count('01234567890123456789'))
