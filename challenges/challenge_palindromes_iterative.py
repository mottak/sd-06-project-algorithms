def is_palindrome_iterative(word):
    """ Dada uma string, retorna se ela é
        um palíndromo usando lógica iterativa. """

    if not word:
        return False
    char_index_to_compare = -1
    for index in range(len(word) // 2):
        if word[index] != word[char_index_to_compare]:
            return False
        else:
            char_index_to_compare -= 1

    return True
