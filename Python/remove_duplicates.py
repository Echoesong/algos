# Maybe try keeping track of the most recent unique number? once I've moved forward in the array, it shouldn't matter what's to the left of me because they are all unique.


def removeDuplicates(nums):
    my_set = set(nums)
    clean_list = list(my_set)
    cache = []
    len_diff = len(nums) - len(clean_list)
    fill = ["."] * len_diff
    clean_list.extend(fill)
    for i, num in enumerate(nums):
        changeable_nums = nums.copy()
        if not nums[i] == clean_list[i]:
            shift = changeable_nums.pop(i)
            cache.append(shift)
    print(f"changeable nums: {changeable_nums}")
    print(f"cache: {cache}")

    pass


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
