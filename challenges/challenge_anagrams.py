def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    return sorted(first_string) == sorted(second_string)
