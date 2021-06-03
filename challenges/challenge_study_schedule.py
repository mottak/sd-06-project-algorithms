def study_schedule(start_time, end_time, target_time):
    has_not_start_time = len(start_time) == 0 or False
    has_not_target_time = target_time is None or False

    if has_not_start_time or has_not_target_time:
        return 0

    target_time_count = 0
    for i in range(len(start_time)):
        if start_time[i] <= target_time <= end_time[i]:
            target_time_count += 1

    return target_time_count


start_time = [2, 1, 2, 1, 4, 4]
end_time = [2, 2, 3, 5, 5, 5]
target_time = 2
print(study_schedule(start_time, end_time, target_time))
