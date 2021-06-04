def study_schedule(start_time, end_time, target_time):
    # Função zip ensinada pelo Bergamini
    counter = 0
    for start, end in zip(start_time, end_time):
        if target_time >= start and target_time <= end:
            counter += 1
    return counter
