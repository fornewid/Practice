def calculate(s):
    def is_sign(c):
        return c == '*' or c == '-' or c == '+' or c == '/'

    def calc(sign, num, others):
        if sign == '+': return num + sum(others)
        if sign == '-': return num - sum(others)
        if sign == '*':
            val = num
            for x in others:
                val *= x
            return val
        if sign == '/':
            val = num
            for x in others:
                val /= x
            return val
        return None

    if s == '(+)':
        return 0

    S = []
    prev = 0
    for c in s:
        if c.isdigit():
            prev = prev * 10 + int(c)
        else:
            if prev != 0:
                S.append(prev)
                prev = 0
            if c == '(' or c == ' ':
                continue
            elif c == ')':
                nums = []
                while not is_sign(S[-1]):
                    nums.append(S.pop(-1))
                S.append(calc(S.pop(-1), nums[-1], nums[:-1]))
            else:
                S.append(c)
    return S[0]

# print(calculate('(- 10 3)'))    # 7
# print(calculate('(- 10 3 5)'))  # 2
# print(calculate('(* 2 3)'))     # 6
# print(calculate('(* 2 3 4)'))  # 24
#
# print(calculate('(* (+ 2 3) (- 5 3))'))  # 10
# print(calculate('(/ (+ 9 1) (+ 2 3))'))  # 2
# print(calculate('(+)'))  # 0
