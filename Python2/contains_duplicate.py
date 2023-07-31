def contains_duplicate(nums):
    my_set = set(nums)
    if len(my_set) == len(nums):
        return False
    else:
        return True


# STOP TRYING TO BE CLEVERRRRRRRRRRR

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(contains_duplicate(nums))
