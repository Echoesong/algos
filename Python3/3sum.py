# Given an integer array nums, return all triplets of different indices that sum to 0


def threeSum(numbers):
    dict = {}
    for i, num in enumerate(numbers):
        dict.update({i: num})
    leftIndex = 0
    rightIndex = len(numbers) - 1
    numbersLength = len(numbers) - 1
    sum = numbers[leftIndex] + numbers[rightIndex]
    target = 0 - sum
    output = []
    while not rightIndex == numbersLength:
        print(
            "left index and value: ",
            leftIndex,
            dict[leftIndex],
            "\nright index and value: ",
            rightIndex,
            dict[rightIndex],
            "\nsum: ",
            sum,
            "\ntarget: ",
            target,
            "\noutput: ",
            output,
        )
        if target in dict.values():
            output.append([dict[leftIndex], dict[rightIndex], target])
        leftIndex += 1
        rightIndex += 1
    return output


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
