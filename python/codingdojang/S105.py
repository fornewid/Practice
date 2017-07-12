def solve(start, end):
    counts = {x: 0 for x in range(0, 10)}

    for x in range(start, end + 1):
        while x > 0:
            counts[x % 10] += 1
            x = int(x / 10)

    return [item for item in counts.items() if item[1] is not 0]

# print(solve(10, 15))
# print(solve(1, 1000))