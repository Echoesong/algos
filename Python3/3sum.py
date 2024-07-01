# Given an integer array nums, return all triplets of different indices that sum to 0


def threeSum(numbers):
    output = []
    numbers.sort()
    anchorIndex = 0
    leftIndex = anchorIndex + 1
    rightIndex = len(numbers) - 1
    while anchorIndex <= len(numbers) - 3:
        target = numbers[anchorIndex] * -1
        sum = numbers[leftIndex] + numbers[rightIndex]
        if rightIndex <= leftIndex:
            # reset
            anchorIndex += 1
            if numbers[anchorIndex] == numbers[anchorIndex - 1]:
                continue
            leftIndex = anchorIndex + 1
            rightIndex = len(numbers) - 1
            target = numbers[anchorIndex] * -1
            sum = numbers[leftIndex] + numbers[rightIndex]
        print(f"target: {target}, sum: {sum}")
        print(f"output: {output}")
        print(f"anchorIndex: {anchorIndex}")
        if sum == target:
            output.append(
                [
                    numbers[anchorIndex],
                    numbers[leftIndex],
                    numbers[rightIndex],
                ]
            )
            anchorIndex += 1
        elif sum > target:
            rightIndex -= 1
        elif sum < target:
            leftIndex += 1

    return output


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
