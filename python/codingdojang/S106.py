def solve(start, end):
    def multiple_of_digit(num):
        val = 1
        while val != 0 and num > 0:
            val *= num % 10
            num = int(num / 10)
        return val

    total = 0
    for i in range(start, end + 1):
        total += multiple_of_digit(i)
    return total

# print(solve(10, 1000))