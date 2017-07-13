def prime_count(n):
    nums = [x for x in range(2, n + 1)]
    for i in range(2, int(n / 2) + 1):
        if i in nums:
            nums = [x for x in nums if x == i or x % i != 0]
            # print(i, nums, sep='\t')
    return len(nums)


# print(prime_count(30))
# print(prime_count(1000))
