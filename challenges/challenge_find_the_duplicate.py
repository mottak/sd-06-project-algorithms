from collections import Counter


def find_duplicate(nums):
    if nums == []:
        return False
    return Counter(nums).most_common()[0][0]
