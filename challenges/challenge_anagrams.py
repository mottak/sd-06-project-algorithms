# def is_anagram(first_string, second_string):
#     first = sorted(first_string)
#     second = sorted(second_string)
#     if first == second:
#         return True
#     else:
#         return False


def is_anagram(first_string, second_string):
    return sorted(first_string) == sorted(second_string)
