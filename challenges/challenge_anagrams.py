def is_anagram(first_string, second_string):
    return sum(ord(s) for s in first_string) == sum(
        ord(s) for s in second_string
    )
