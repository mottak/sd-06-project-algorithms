def study_schedule(start_time, end_time, target_time):
    if len(start_time) + len(end_time) + target_time == 0:
        return 0

    counter = 0
    for n in range(len(start_time)):
        if start_time[n] <= target_time <= end_time[n]:
            counter += 1

    return counter
