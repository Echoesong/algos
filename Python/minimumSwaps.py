# Sorting problem.
# Any 2 numbers can swap, including numbers that have swapped before, though idk if we would ever wanna do that
# Brute force: Iterate over array to find element = i + 1, swap it with element at i position.
# for : if array[i] == i + 1, continue, else: for j in range(i + 1)

# Add all numbers to a dictionary where key = index and value = value
# For each pair in the dictionary, if key != key + 1, then:
#   append cache


def minimumSwaps(arr):
    swaps = 0
    dictionary = {}

    for i, num in enumerate(arr):
        dictionary.update({i: num - 1})
    print(dictionary)
    for key in list(dictionary.keys()):
        while not dictionary[key] == key:
            cache = dictionary[key]
            dictionary[key], dictionary[cache] = dictionary[cache], dictionary[key]
        swaps += 1

    return swaps


arr0 = [1, 2, 3, 4]
arr1 = [4, 3, 1, 2]
arr2 = [7, 1, 3, 2, 4, 5, 6]  # Expected output: 5
arr3 = [1, 3, 5, 2, 4, 6, 7]  # Expected output: 3
print(minimumSwaps(arr2))
