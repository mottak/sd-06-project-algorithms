def study_schedule(start_time, end_time, target_time):
    best_time = 0
    if start_time == [] or target_time == 0:
        return 0
    for x1, x2 in zip(start_time, end_time):
        if target_time >= x1 and target_time <= x2:
            best_time += 1
    return best_time


start_time = [2, 1, 2, 1, 4, 4]
end_time = [2, 2, 3, 5, 5, 5]
print(study_schedule(start_time, end_time, 5))
