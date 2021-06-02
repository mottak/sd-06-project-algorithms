def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False
    first = sorted(first_string)
    second = sorted(second_string)
    if first != second:
        return False
    return True
