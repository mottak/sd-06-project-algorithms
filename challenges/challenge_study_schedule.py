def study_schedule(start_time, end_time, target_time):
    if start_time == 0 or target_time == 0:
        return 0

    count = 0

    for x in range(0, len(start_time)):
        index = start_time[x]

        while index <= end_time[x]:
            if index == target_time:
                count += 1
            index += 1

    return count
