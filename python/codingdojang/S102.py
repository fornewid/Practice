import functools
def max_num(items):
    def compare(x, y):
        return 1 if x + y < y + x else -1
    items = [str(x) for x in items]
    items.sort(key=functools.cmp_to_key(compare))
    return ''.join(items)

# print(max_num([1, 2, 3]))
# print(max_num([3, 30, 34, 5, 9]))
