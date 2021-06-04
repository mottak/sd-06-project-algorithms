def is_palindrome_recursive(word, low, high):
    if word:
        if low == high or low > high:
            return True
        elif word[low] != word[high]:
            return False
        else:
            return is_palindrome_recursive(word, low + 1, high - 1)
    else:
        return False
