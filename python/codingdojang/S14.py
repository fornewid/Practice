def solve(s):
    data = s.split(' ')
    items = data[1:]
    rot = int(data[0]) % len(items)
    return items[rot:] + items[:rot]

# print(solve('2 a b c d e'))
# print(solve('0 똘기 떵이 호치 새초미'))