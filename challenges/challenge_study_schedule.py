def study_schedule(start_time, end_time, target_time):
    if len(start_time) + len(end_time) + target_time == 0:
        return 0

    return sum(
        start_time[n] <= target_time <= end_time[n]
        for n in range(len(start_time))
    )
