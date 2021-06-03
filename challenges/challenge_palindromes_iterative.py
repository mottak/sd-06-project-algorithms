def is_palindrome_iterative(word):
    if word == "":
        return False
    return list(word) == list(reversed(word))
