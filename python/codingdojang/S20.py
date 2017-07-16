def page_count(m, n):
    return m // n + (m % n != 0)

# print(page_count(0, 1) == 0)
# print(page_count(1, 1) == 1)
# print(page_count(2, 1) == 2)
# print(page_count(1, 10) == 1)
# print(page_count(10, 10) == 1)
# print(page_count(11, 10) == 2)
