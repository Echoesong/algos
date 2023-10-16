def containsDuplicates(nums):
    mySet = set()
    for num in nums:
        print(num)
        if num in mySet:
            return True
        mySet.add(num)
    else:
        return True


nums = [1, 2, 3, 1]
print(containsDuplicates(nums))
