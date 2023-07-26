def removeDuplicates(nums):
    my_set = set(())
    test_set = set(nums)
    for num in reversed(nums):
        if num not in (my_set):
            my_set.add(num)
        else:
            nums.pop(num)

    print(my_set, nums, test_set)
    return len(nums)


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
