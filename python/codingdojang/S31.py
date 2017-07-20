def how_many(time_logs, target):
    man_count = 0
    for time_log in time_logs.split('\n'):
        time = time_log.split()
        if time[0] <= target and target < time[1]:
            man_count += 1
            # print(time)
    return man_count

time_logs = '09:12:23 11:14:35\n10:34:01 13:23:40\n10:34:31 11:20:10'
target_time = '11:05:20'
# print(how_many(time_logs, target_time))
