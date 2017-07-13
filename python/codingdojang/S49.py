import queue

def get_ugly_number(n):
    output, pre_defined = [], [2, 3, 5]
    check = {1}
    PQ = queue.PriorityQueue()
    PQ.put(1)

    for i in range(n):
        new = PQ.get()
        output.append(new)

        for x in pre_defined:
            val = x * new
            if val not in check:
                PQ.put(val)
                check.add(val)
    # print(output)
    # print(check)
    return output[-1]

# print(get_ugly_number(1500) == 859963392)
# print(get_ugly_number(1550) == 1093500000)
# print(get_ugly_number(100000) == 290142196707511001929482240000000000000)
