def solve(max):
    total = 0
    non_self = set()
    for x in range(1, max + 1):
        if x not in non_self:
            total += x
        non_self.add(x + eval('+'.join(str(x))))
    return total