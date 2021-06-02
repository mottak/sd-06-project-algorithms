from collections import Counter

def find_duplicate(nums):
    if len(nums) <= 1 or type(nums) == str:
        return False
    mode = Counter(nums).most_common()
    return mode[0][0]
