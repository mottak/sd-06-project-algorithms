#!/usr/bin/env python3
def is_character_equal(a, b):
    if (a == b):
        return True
    return False


def is_palindrome_recursive(word, low, high):
    mid_point = len(word) // 2
    if not word:
        return False

    if len(word) == 1:
        return True

    result = is_character_equal(word[low], word[high])

    if (low + 1 == mid_point):
        return result

    return is_palindrome_recursive(word, low + 1, high - 1)


word = 'ARARA'
print(is_palindrome_recursive(word, 0, len(word) - 1))
