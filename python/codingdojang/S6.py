def count_of_eight_queens():
    def can_choose(columns, new_c):
        new_r = len(columns)
        for r in range(len(columns)):
            c = columns[r]
            if new_c == c or abs(new_r - r) == abs(new_c - c):
                return False
        return True

    def choose_in(columns, items):
        if not items:
            nonlocal count
            count += 1
            # print(columns)
            return
        for col_idx in range(len(items)):
            col = items[col_idx]
            if can_choose(columns, col):
                columns.append(col)
                choose_in(columns, items[0:col_idx] + items[col_idx+1:])
                columns.remove(col)

    count = 0
    columns = []
    items = [i for i in range(8)]
    choose_in(columns, items)
    return count


# print(count_of_eight_queens())
