def longest_common_substring(s1, s2):
    if len(s1) < len(s2):
        tmp = s1
        s1 = s2
        s2 = tmp

    for size in range(len(s2), 0, -1):
        for s in range(len(s2) - size + 1):
            # print(s, s+size, s2[s:s+size])
            if s2[s:s+size] in s1:
                return s2[s:s+size]

s1 = 'photography'
s2 = 'autograph'
longest = longest_common_substring(s1, s2)
# print(len(longest), longest, sep='\n')
