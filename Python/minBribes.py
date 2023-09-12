def minimumBribes(array):
    bribes = 0
    for i in range(len(array) - 1):
        if (array[i] - i) > 3:
            # We do > 3 rather than > 2 because the values are going to be one higher than their original index by default
            print("Too Chaotic")
            return
        for j in range(i, min(i + 3, len(array))):
            # This is supposed to make a smaller loop checking the next 2 index values, or the end of the array, whichever comes first.
            if array[j] < array[i]:
                bribes += 1
    print(bribes)


q = [1, 2, 5, 3, 4, 7, 8, 6]
q2 = [4, 1, 2, 3]
q3 = [1, 2, 5, 3, 7, 8, 6, 4]

minimumBribes(q3)
