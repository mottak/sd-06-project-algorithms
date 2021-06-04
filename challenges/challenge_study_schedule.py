def study_schedule(start_time, end_time, target_time):
    """
    Find zip function (https://realpython.com/python-zip-function/),
    zip works as a parallel iterator (Tuple iterator)
    """
    counter = 0
    for tempo1, tempo2 in zip(start_time, end_time):
        if target_time >= tempo1 and target_time <= tempo2:
            counter += 1
    return counter
