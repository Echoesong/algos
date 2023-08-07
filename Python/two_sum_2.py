def twoSum(numbers, target):
    leftPointer = 0
    rightPointer = len(numbers) - 1
    while leftPointer <= rightPointer:
        sum = numbers[leftPointer] + numbers[rightPointer]
        print("pointers: ", leftPointer, rightPointer)
        print("sum: ", sum)
        if sum == target:
            return [leftPointer, rightPointer]
        elif sum < target:
            leftPointer += 1
        elif sum > target:
            rightPointer -= 1
    return


numbers = [2, 7, 11, 15]
target = 9

twoSum(numbers, target)
