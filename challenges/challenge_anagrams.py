def is_anagram(first_string, second_string):
    """Faça o código aqui. Iniciando"""
    if not first_string or not second_string:
        return False
    if sorted(first_string) == sorted(second_string):
        return True
    else:
        return False
