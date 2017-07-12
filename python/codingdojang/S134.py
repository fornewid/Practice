def solve(max_val):
    def fib(limit):
        a = [1,1]
        while a[1] < limit:
            yield a[1]
            a.reverse()
            a[1] += a[0]

    return sum(x for x in fib(max_val) if x % 2 == 0)

# print(solve(4000000))