#!/usr/bin/env python3

def study_schedule(start_time, end_time, target_time):
    if (not start_time or not end_time):
        return 0

    count = 0
    for start, end in zip(start_time, end_time):
        if (start <= target_time and end >= target_time):
            count += 1

    return count


start_time = [4, 1, 3, 2]
end_time = [4, 3, 4, 5]

# print(study_schedule(start_time, end_time, 3))
