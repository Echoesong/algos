from typing import List

def topKFrequent(nums, k):
    dict = {}
    iterable_nums = tuple(nums)
    for num in iterable_nums:
        # if number exists in dictionary, increase value by 1
        # if number does not exist in dictionary, create it as a new key and set value to 1
        if dict.get(num):
            dict[num] += 1
        else:
            dict.update({num: 1})
    my_array = list(dict.values())
    my_array.sort()
    result = []
    i = 0
    while(i<k):
        result.append(my_array[0])
        my_array.pop(0)
        i += 1
    return result

nums = [-1, -1]
k = 1

print(topKFrequent(nums, k))