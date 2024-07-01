def containsDuplicates(nums):
    mySet = set()
    for num in nums:
        mySet.add(num)
    if not len(mySet) == len(nums):
        return True
    else:
        return False


nums = [1, 2, 3, 4]
print(containsDuplicates(nums))
