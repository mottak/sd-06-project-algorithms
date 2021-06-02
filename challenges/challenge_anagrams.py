def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    if len(first_string) == len(second_string):
        if sorted(first_string) == sorted(second_string):
            return True
        else:
            return False
    else:
        return False

# baseado no site abaixo:
# https://www.programiz.com/python-programming/examples/anagram
