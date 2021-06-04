def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '' or len(first_string) != len(second_string):
        return False

    for x in range(0, len(first_string)):
        if first_string[x] not in second_string:
            return False
    
    return True
