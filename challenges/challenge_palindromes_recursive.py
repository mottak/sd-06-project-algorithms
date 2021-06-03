def is_palindrome_recursive(word, low, high):
    # Dado uma string, determine se ela é um palíndromo ou não.
    # Se for passado uma string vazia, retorne False;
    if not word:
        return False

    # Se assemelha ao exercício com listas dia 37.1
    # low seria a última letra para testar com high a primeira
    if word[high] == word[low]:
        # aqui a varredura pela palavra acaba \/
        if high <= low:
            return True
            # a func se repete aumentando (+1) passo para low e diminuindo
            # (-1) passo para high até que high seja menor que low ou low seja
            # maior que high, ou seja a varredura pela palavra terminou.
        return is_palindrome_recursive(word, low + 1, high - 1)
    return False
