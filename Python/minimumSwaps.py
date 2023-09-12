# Sorting problem.
# Any 2 numbers can swap, including numbers that have swapped before, though idk if we would ever wanna do that
# Brute force: Iterate over array to find element = i + 1, swap it with element at i position.
# for : if array[i] == i + 1, continue, else: for j in range(i + 1)


# Brute force solution:
def minimumSwaps(arr):
    swaps = 0
    dictionary = {}
    for i, num in enumerate(arr):
        if num == i + 1:
            continue
        else:
            # i + 1 = correct number, num = wrong number
            if num in dictionary:
                dictionary.update({num: i + 1})
                arr[i] = dictionary[num]
                swaps -= 1
            else:
                dictionary.update({num: None})
                swaps += 1
    return swaps


arr0 = [1, 2, 3, 4]
arr1 = [4, 3, 1, 2]
arr2 = [7, 1, 3, 2, 4, 5, 6]  # Expected output: 5
arr3 = [1, 3, 5, 2, 4, 6, 7]  # Expected output: 3
print(minimumSwaps(arr2))
