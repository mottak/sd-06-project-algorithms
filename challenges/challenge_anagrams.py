from random import randint


def quicksort(string):
    # stops recursive loop
    if len(string) < 2:
        return string

    # Select `pivot` randomly
    pivot = string[randint(0, len(string) - 1)]

    low, same, high = [], [], []
    for item in string:
        # Elements are divided between 'low', 'same'
        # or 'high'(er) than pivot value.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)

    # Combines the sorted `low` list with the
    # `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)


def is_anagram(first_string, second_string):
    """ Compares two strings and returns if they are anagrams
        using quicksort algorithm. """
    # https://realpython.com/sorting-algorithms-python/#the-timsort-algorithm-in-python
    if not first_string or not second_string or (
        len(first_string) != len(second_string)
    ):
        return False

    sort_first_string = quicksort(first_string)
    sort_second_string = quicksort(second_string)

    for index, char in enumerate(sort_first_string):
        if char != sort_second_string[index]:
            return False
    return True
