def is_anagram(first_string, second_string):
    # Retorne false se a primeira ou a segunda palavra for uma string vazia
    if not first_string or not second_string:
        return False

    if len(first_string) != len(second_string):
        return False
    for letra in first_string:
        if letra not in second_string:
            return False
    return True
