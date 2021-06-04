def study_schedule(start_time, end_time, target_time):
    melhor_horario = 0
    # A zip()função retorna um objeto zip, que é um iterador de tuplas
    # em que o primeiro item em cada iterador passado é pareado e,
    # em seguida, o segundo item em cada iterador passado é pareado etc.
    # https://www.w3schools.com/python/ref_func_zip.asp
    # https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s15.html
    for tempo1, tempo2 in zip(start_time, end_time):
        if target_time >= tempo1 and target_time <= tempo2:
            melhor_horario += 1
    return melhor_horario
