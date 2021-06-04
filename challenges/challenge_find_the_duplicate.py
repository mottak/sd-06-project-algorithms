def find_duplicate(nums):
    if len(nums) <= 1 or not any(f"{s}".isnumeric() for s in nums):
        return False

    return max(set(nums), key=nums.count)
