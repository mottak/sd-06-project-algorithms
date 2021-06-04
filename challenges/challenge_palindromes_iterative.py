#!/usr/bin/env python3
def is_palindrome_iterative(word):
    if not word:
        return False

    counter = 0
    high = len(word) - 1
    mid_point = len(word) // 2

    while counter < mid_point:
        if word[counter] != word[high - counter]:
            return False
        counter += 1
        if (counter == mid_point):
            return True


print(is_palindrome_iterative('ANA'))
