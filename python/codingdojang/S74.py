import math
def count_of_suffix_0(n, x=5):
    return sum(int(n / (x ** (i+1))) for i in range(int(math.log(n, x))))

# print(count_of_suffix_0(12))
# print(count_of_suffix_0(25))