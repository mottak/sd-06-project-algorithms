from collections import Counter

# start_time = [2, 4, 2, 1, 4, 4]
# end_time = [2, 2, 3, 5, 5, 5]

def study_schedule(start_time, end_time, target_time):
    schedule = { "1": 0, "2": 0, "3":0, "4":0, "5":0 }

    for st, et in zip(start_time, end_time):
        isInRange = (target_time >= st) and (target_time <= et)
        if isInRange:
            if target_time == 1:
                schedule["1"] += 1
            if target_time == 2:
                schedule["2"] += 1
            if target_time == 3:
                schedule["3"] += 1
            if target_time == 4:
                schedule["4"] += 1
            if target_time == 5:
                schedule["5"] += 1

    counter = Counter(schedule)

    return counter.most_common(1)[0][1]

# study_schedule(start_time, end_time, 4)