def is_palindrome_recursive(word, low, high):
    """ Faça o código aqui. """
    if not word:
        return False

    if word[low] != word[high]:
        return False
    elif low == high or low - high == 1:
        return True
    else:
        return is_palindrome_recursive(word, low + 1, high - 1)
