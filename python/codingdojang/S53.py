n, items = int(input()), []
for i in range(n):
    items.append([int(x) for x in input().split()])
items.sort(key=lambda x: x[0])

result = []
for x in items:
    if result and result[-1][1] >= x[0]:
        result[-1][1] = max(result[-1][1], x[1])
    else:
        result.append(x)

for x in result:
    print('%d %d' % (x[0], x[1]))
