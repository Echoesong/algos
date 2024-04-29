def containsDuplicates(self, nums):
    mySet = set()
    for num in nums:
        mySet.add(num)
    if len(mySet) == len(nums):
        return True
    else:
        return False
