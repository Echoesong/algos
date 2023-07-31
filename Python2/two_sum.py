def twoSum(nums, target):
    left_dict = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in left_dict:
            return [i, left_dict[diff]]
        else:
            left_dict[num] = i


nums = [2, 7, 11, 15]

target = 9

print(twoSum(nums, target))
