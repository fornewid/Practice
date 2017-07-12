def solve(n):
    for i in range(1, n + 1):
        print('O' * (n - i) + 'X' * i)

# solve(6)
# solve(int(input()))