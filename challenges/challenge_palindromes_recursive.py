def is_palindrome_recursive(word, low, high):
    """ Resumo: Função recursiva é aquela que invoca a si mesma.
    Em programação, a recursividade é um mecanismo útil e
    poderoso que permite a uma função chamar a si mesma direta
    ou indiretamente, ou seja, uma função é dita recursiva se
    ela contém pelo menos uma chamada explícita ou implícita a si própria.
    Prof. Wellington Lima dos Santos (Unicamp) """
    if word == "":
        return False
    if word[low] != word[high]:
        return False
    if low == high:
        return True
    if low < high:
        return is_palindrome_recursive(word, low + 1, high - 1)
