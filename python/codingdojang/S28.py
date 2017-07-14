def special_sort(items):
    return [x for x in items if x < 0] + [x for x in items if x >= 0]

# print(special_sort([-1, 1, 3, -2, 2]))
# print([-1, -2, 1, 3, 2])
