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
    x = dict.items()
    x_list = list(x)
    sorted_x_list = sorted(x_list, key=lambda x:x[1], reverse=True)
    result = []
    i = 0
    while i < k:
        to_add = sorted_x_list.pop(0)
        list(to_add)
        result.append(to_add[0])
        i += 1
    return result

nums = [4,1,-1,2,-1,2,3]
k = 2

print(topKFrequent(nums, k))