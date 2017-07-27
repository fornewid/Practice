def OneEditApart(s1, s2):
    if len(s1) > len(s2):
        temp = s1
        s1 = s2
        s2 = temp

    # 변환
    if len(s1) == len(s2):
        return 1 >= len([pair for pair in zip(s1, s2) if pair[0] != pair[1]])
    # 추가 or 삭제
    elif len(s1) + 1 == len(s2):
        for i, c in enumerate(s1):
            if s2[i] != c:
                return s1[i:] == s2[i+1:]
        return True
    return False

print(OneEditApart('cat', 'dog') is False)
print(OneEditApart('cat', 'cats') is True)
print(OneEditApart('cat', 'cut') is True)
print(OneEditApart('cat', 'cast') is True)
print(OneEditApart('cat', 'at') is True)
print(OneEditApart('cat', 'acts') is False)
