def partition(array, start, end):
    i = start - 1
    pivot = array[end]

    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[j], array[i] = array[i], array[j]

    array[i + 1], array[end] = array[end], array[i + 1]

    return i + 1


def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    if len(array) == 1:
        return array

    if start < end:
        partition_index = partition(array, start, end)

        quicksort(array, start, partition_index - 1)
        quicksort(array, partition_index + 1, end)


def is_anagram(first_string, second_string):
    list1 = list(first_string)
    list2 = list(second_string)
    quicksort(list1)
    quicksort(list2)

    return list2 == list1
