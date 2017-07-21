n = int(input())
sum = 0
for i in range(n):
    sum += int(input())
avg = sum / n
print("sum: %d, avg: %.2f" % (sum, avg))