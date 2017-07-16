def dash_insert(s):
    def is_even(num):
        return num is not None and num != 0 and num % 2 == 0
    def is_odd(num):
        return num is not None and num != 0 and num % 2 != 0

    new = []
    for c in s:
        prev = int(new[-1]) if new else None
        curr = int(c)
        if is_even(curr) and is_even(prev):
            new.append('*')
        if is_odd(curr) and is_odd(prev):
            new.append('-')
        new.append(c)

    return ''.join(new)


# print(dash_insert('4546793') == "454*67-9-3")
# print(dash_insert('02') == "02")
