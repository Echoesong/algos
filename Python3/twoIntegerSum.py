# non-decreasing order means next index is equal to or greater than current
# OUTPUT is an array of index values, e.g. [1, 2]
# INPUT is array of ints, target int


def twoIntegerSum(numbers, target):
    leftIndex = 0
    rightIndex = len(numbers) - 1
    sum = numbers[leftIndex] + numbers[rightIndex]
    output = []

    while not sum == target and not leftIndex >= rightIndex:
        if sum == target:
            output = [leftIndex, rightIndex]
        elif sum > target:
            rightIndex -= 1
            sum = numbers[leftIndex] + numbers[rightIndex]
        elif sum < target:
            leftIndex += 1
            sum = numbers[leftIndex] + numbers[rightIndex]
    if sum == target:
        output = [leftIndex + 1, rightIndex + 1]
    return output
