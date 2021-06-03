def study_schedule(start_time, end_time, target_time):
    if start_time == 0 or target_time == 0:
        return 0

    count = 0

    for x in range(0, len(start_time)):
        if target_time >= start_time[x] and target_time <= end_time[x]:
            count += 1

    return count
