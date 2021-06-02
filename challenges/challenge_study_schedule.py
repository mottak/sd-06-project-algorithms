def study_schedule(start_time, end_time, target_time):
    conta_estudante = 0
    if start_time == [] or target_time == 0:
        return 0
    for start, end in zip(start_time, end_time):
        if target_time >= start and target_time <= end:
            conta_estudante += 1
    return conta_estudante

# https://www.w3schools.com/python/ref_func_zip.asp
# a Função zip() retorna um zip object, que é um itrador de
# tuplas,onde o primeiro item do iterador
# é emparelhado ao primeiro array e o segundo item do iterador
# é emparelhado com o segundo array
