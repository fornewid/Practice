def solve(max_val):
    def fib(limit):
        a = [0,1]
        while a[0] < limit:
            yield a[0]
            a.reverse()
            a[1] += a[0]

    for x in fib(max_val + 1):
        print(x)