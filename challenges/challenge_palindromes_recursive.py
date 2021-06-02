def is_palindrome_recursive(word, low, high):
    """ Dada uma string, retorna se ela é um palíndromo
        usando recursividade. """

    if not word:
        return False
    if len(word) <= 3:
        return word[low] == word[high]
    if word[low] == word[high]:
        return is_palindrome_recursive(word[1:-1], low, high - 2)
    return False
