def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) != len(second_string):
        return False
    for i in second_string:
        if i not in first_string:
            return False
    return True
