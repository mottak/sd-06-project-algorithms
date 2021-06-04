def is_palindrome_recursive(word, low, high):
    if word == "" or word[low] != word[high]:
        return False

    if len(word) == 1:
        return True

    cut = word[1:-1]
    return is_palindrome_recursive(cut, 0, len(cut) - 1)
