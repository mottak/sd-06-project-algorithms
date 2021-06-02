def study_schedule(start_time, end_time, target_time):
    counter = 0

    if not target_time:
        return 0

    for start_t, stop_t in zip(start_time, end_time):
        if start_t <= target_time <= stop_t:
            counter += 1

    return counter
