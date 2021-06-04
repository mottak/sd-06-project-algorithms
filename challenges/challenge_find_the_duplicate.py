def find_duplicate(nums):
    if len(nums) < 2:
        return False

    counter = {}

    for num in nums:
        try:
            int(num)
        except ValueError:
            return False

        if (num) <= 0:
            return False

        if num in counter:
            return num

        counter[num] = 1

    return False
