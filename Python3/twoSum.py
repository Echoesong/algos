def twoSum(nums, target):
    nums.sort()
    point1 = 0
    point2 = len(nums) - 1
    diff = nums[point2] - nums[point1]
    while not point1 == point2:
        print("diff: ", diff)
        if diff > target:
            point2 -= 1
        elif diff < target:
            point1 += 1
        else:
            return [point1, point2]


testArray = [3, 4, 5, 6]
targetNum = 7

print(twoSum(testArray, targetNum))
