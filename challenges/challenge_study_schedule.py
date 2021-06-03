def study_schedule(start_time, end_time, target_time):
    """Busca horário menos utilizado pelos estudantes"""

    same_time_students = 0

    for student_start, student_end in zip(start_time, end_time):
        if target_time >= student_start and target_time <= student_end:
            same_time_students += 1
    return same_time_students
