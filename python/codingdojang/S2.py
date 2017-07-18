def print_spiral_array(m, n):
    array = [[-1 for _ in range(n)] for _ in range(m)]

    x, y, invalid = 0, 0, -1
    steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    curr = 0

    for i in range(m * n):
        # print(i, x, y)
        array[x][y] = i
        new_x, new_y = x + steps[curr][0], y + steps[curr][1]

        # collision
        if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or array[new_x][new_y] != invalid:
            curr = (curr + 1) % len(steps)
            new_x, new_y = x + steps[curr][0], y + steps[curr][1]
        x, y = new_x, new_y

    for row in array:
        for item in row:
            print('%4s' % item, end='')
        print()
    print()

# print_spiral_array(6, 6)
# print_spiral_array(4, 6)
