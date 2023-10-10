def leftRotation(a, d):
    dictionary = {}
    for i, number in enumerate(range(1, a + 1)):
        dictionary.update({number: i})

    print(dictionary)


a = 5
d = 4

leftRotation(a, d)
