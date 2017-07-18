input = '''1 2 4 4\n2 3 5 7\n3 1 6 5\n7 3 8 6'''

def rect_area_BF(input):
    rect_set = set()
    for rect_str in input.split('\n'):
        rect = [int(c) for c in rect_str.split()]
        for x in range(rect[0], rect[2]):
            for y in range(rect[1], rect[3]):
                rect_set.add((x, y))
    return len(rect_set)

print(rect_area_BF(input))
