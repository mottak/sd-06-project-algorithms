def is_palindrome_recursive(word, low, high):
    """ Faça o código aqui. """
    if word == '':
        return False
    if word[low] != word[high]:
        return False
    if len(word) == 1:
        return True
    if low < high:
        low += 1
        high -= 1
        return is_palindrome_recursive(word, low, high)
