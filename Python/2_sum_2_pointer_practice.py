def two_sum(nums, target):
    i = 0
    j = len(nums) - 1
    while not i == j:
        sum = nums[i] + nums[j]
        print(f"sum: {sum} i: {i}, j: {j}")
        if sum == target:
            return [i, j]
        elif sum < target:
            i += 1
        elif sum > target:
            j -= 1


# Okay so we need to use two pointers, i at the start j at the end. If i+j = target, return index values. If it is greater than target, decrement j. If it is less than target, increment i. If i == j and no answer, return none.


nums = [3, 2, 4]
target = 6
print(two_sum(nums, target))
