def solve(n):
    def sum_of_multiples(k, max):
        n = int((max - 1) / k)
        return k * int(n * (n + 1) / 2)

    return sum_of_multiples(3, n) + sum_of_multiples(5, n) - sum_of_multiples(15, n)