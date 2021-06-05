def find_duplicate(nums):
    for i, num in enumerate(nums):
        try:
            nums.index(num, i + 1)
            return num
        except ValueError:
            continue

    return False
