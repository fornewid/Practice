def is_balanced(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif not stack:
            return False
        else:
            stack.pop(-1)
        # print(c, stack, sep='\t')
    return False if stack else True


# print(is_balanced('(()()()())') is True)
# print(is_balanced('(((())))') is True)
# print(is_balanced('(()((())()))') is True)
# print(is_balanced('((((((())') is False)
# print(is_balanced('()))') is False)
# print(is_balanced('(()()(()') is False)
# print(is_balanced('(()))(') is False)
# print(is_balanced('())(()') is False)
