def find_duplicate(nums):
    if not nums:
        return False

    nums_arr = nums.copy()
    nums_arr.sort()

    for index, number in enumerate(nums_arr):
        if index == len(nums_arr) - 1:
            break

        if number == nums_arr[index + 1]:
            return number

    return False
