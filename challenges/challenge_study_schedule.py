from typing import Counter


def study_schedule(start_time, end_time, target_time):
    """ Recebe um horário target_time e retorna quantos estudantes
        estavam estudando naquele horário. """
    if not target_time or  not start_time:
        return 0

    counter = 0
    for index, hour in enumerate(start_time):
        if target_time >= hour and target_time <= end_time[index]:
            counter += 1

    return counter
