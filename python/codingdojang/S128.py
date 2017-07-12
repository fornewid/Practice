def solve(n):
    def is_complete(num):
        return num == sum(x for x in range(1, int(num / 2 + 1)) if num % x is 0)

    print([x for x in range(1, n + 1) if is_complete(x)])