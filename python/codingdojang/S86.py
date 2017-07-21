def print_art_n(n):
    basic = ''.join(['N' if _ == 0 or _ == n-1 else ' ' for _ in range(n)])
    for i in range(n):
        print(basic[:i] + 'N' + basic[i+1:])

# for i in range(1, 8, 2):
#     print_art_n(i)
#     print()
