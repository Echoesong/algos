def rotLeft(a, d):
    indices = []
    output = []
    for i, number in enumerate(range(1, a + 1)):
        output.append(number)
        j = i - d
        indices.append(j)
    output2 = output.copy()
    for i, number in enumerate(output):
        output2[indices[i]] = number

    return output2


a = 5
d = 4

leftRotation(a, d)
