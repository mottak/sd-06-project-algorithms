def is_palindrome_recursive(word, low, high):
    if low == high:
        return True
    if word == "" or word[low] != word[high]:
        return False

    return is_palindrome_recursive(word, low + 1, high - 1)
