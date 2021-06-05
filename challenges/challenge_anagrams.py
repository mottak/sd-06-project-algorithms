# https://realpython.com/sorting-algorithms-python/#the-timsort-algorithm-in-python

def insertion_sort(array, min, max):
    for i in range(min + 1, max + 1):
        item = array[i]
        j = i - 1
        while j >= min and array[j] > item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item

    return array


def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1

        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def timsort(array):
    min_run = 32
    n = len(array)
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))

            merged_array = merge(
                left=array[start:mid + 1], right=array[mid + 1:end + 1])

            array[start:start + len(merged_array)] = merged_array

        size *= 2

    return array


def is_anagram(first_string, second_string):
    decimal_first_string = list(map(lambda x: ord(x), list(first_string)))
    decimal_second_string = list(map(lambda x: ord(x), list(second_string)))

    if(timsort(decimal_first_string) == timsort(decimal_second_string)):
        return True
    return False
