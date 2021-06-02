def study_schedule(start_time, end_time, target_time):
    counter = 0
    if start_time == [] or target_time == 0:
        return 0

    for index, hour in enumerate(start_time):
        if target_time <= end_time[index] and target_time >= hour:
            counter += 1

    return counter
