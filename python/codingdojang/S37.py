def check_jolly_jumper(s):
    items = [int(c) for c in s.split(' ')[1:]]
    diffs_set = {abs(items[i - 1] - items[i]) for i in range(1, len(items))}
    # print(diffs_set)

    if len(diffs_set) == len(items) - 1\
            and min(diffs_set) == 1\
            and max(diffs_set) == len(items) - 1:
        return 'Jolly'
    else:
        return 'Not jolly'

# print(check_jolly_jumper('4 1 4 2 3') == 'Jolly')
# print(check_jolly_jumper('5 1 4 2 -1 6') == 'Not jolly')
