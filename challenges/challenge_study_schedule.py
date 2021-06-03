def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    list = []
    for start_time, end_time in zip(start_time, end_time):
        list.append((start_time, end_time))

    cont_result = 0
    for item in list:
        if item[0] <= target_time <= item[1]:
            cont_result += 1
    return cont_result
