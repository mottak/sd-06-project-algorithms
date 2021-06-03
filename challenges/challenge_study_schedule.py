def study_schedule(start_time, end_time, target_time):
    """Busca horário menos utilizado pelos estudantes"""

    same_time_students = 0

    for student_start_time, student_end_time in zip(start_time, end_time):
        if target_time >= student_start_time and target_time <= student_end_time:
            same_time_students += 1
    return same_time_students