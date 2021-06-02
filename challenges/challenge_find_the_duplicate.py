from challenges.challenge_anagrams import quicksort

def find_duplicate(nums):
    """ Recebe uma lista de números inteiros >= 1 como parâmetro,
        ordena e retorna um número se ele for repetido na lista """
    if not nums or isinstance(nums, str) or len(nums) < 2:
        return False

    sort_nums = quicksort(nums)

    if sort_nums[0] == sort_nums[1]:
        return sort_nums[0]
    next_step = sort_nums[1:]
    return find_duplicate(next_step)
