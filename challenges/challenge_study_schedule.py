def study_schedule(start_time, end_time, target_time):
    counter = 0
    for start, end in zip(start_time, end_time):
        # best schedule  --
        distance = (target_time >= start) and (target_time <= end)
        # best schedule = true ++counter
        if distance:
            counter += 1

    return counter
