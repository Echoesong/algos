def rotLeft(a, d):
    n = len(a)
    output = [0] * n
    for i, number in enumerate(a):
        newIndex = i - d
        output[newIndex] = number

    return output


a = 5
d = 4

leftRotation(a, d)
