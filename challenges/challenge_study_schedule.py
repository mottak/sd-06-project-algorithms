def study_schedule(start_time, end_time, target_time):
    count = 0
    if start_time == [] or end_time == []:
        return 0
    for i in range(len(end_time)):
        if end_time[i] >= target_time >= start_time[i]:
            count += 1

    return count
