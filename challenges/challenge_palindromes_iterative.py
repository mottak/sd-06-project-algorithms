def is_palindrome_iterative(word):
    if (word != word[::-1] or word == ""):
        return False

    return True
