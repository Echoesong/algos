# Sorting problem.
# Any 2 numbers can swap, including numbers that have swapped before, though idk if we would ever wanna do that
# Brute force: Iterate over array to find element = i + 1, swap it with element at i position.
# for : if array[i] == i + 1, continue, else: for j in range(i + 1)


def minimumSwaps(arr):
    swaps = 0
    for i, num in enumerate(arr):
        if num == i + 1:
            continue
        else:
            for j in range(len(arr) - i):
                if arr[j] == i + 1:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
                    print(arr)


arr1 = [4, 3, 1, 2]
arr2 = [7, 1, 3, 2, 4, 5, 6]  # Expected output: 5
print(minimumSwaps(arr1))
