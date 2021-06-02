def study_schedule(start_time, end_time, target_time):
    occurrences = 0
    for st, et in zip(start_time, end_time):
        isInRange = (target_time >= st) and (target_time <= et)
        if isInRange:
            occurrences += 1

    return occurrences
