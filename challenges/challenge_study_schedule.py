def study_schedule(start_time=[], end_time=[], target_time=[]):
    contador = 0

    if not target_time or not start_time or not end_time:
        return contador

    for indice in range(len(end_time)):
        if start_time[indice] <= target_time <= end_time[indice]:
            contador += 1
    return contador
