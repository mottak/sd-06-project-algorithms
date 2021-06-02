def study_schedule(start_time, end_time, target_time):
    best_time = 0
    if start_time == [] or target_time == 0:
        return 0
    # zip joins two arrays over just one iteration
    for x1, x2 in zip(start_time, end_time):
        if target_time >= x1 and target_time <= x2:
            best_time += 1
    return best_time
