def is_palindrome_iterative(word):
    # A funções iterativa dependem de uma condição ser
    # verdadeira ou falsa para iniciar ou interromper a repetição.
    # Neste exemplo fiz sem FOR
    # Macete do fatiamento que aprendi com o Guanabara
    # https://www.youtube.com/watch?v=5VBWe6BXzRo
    if word and word == word[::-1]:
        return True
    return False
