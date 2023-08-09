def gameWinner(colors):
    colorsList = list(colors)
    wendy = []
    bob = []
    wCounter = 0
    bCounter = 0
    lPointer = 0
    rPointer = 1
    print(colorsList)
    for i in range((len(colors) - 1)):
        currentEl = colors[i]
        nextEl = colors[i + 1]
        if currentEl == nextEl:
            if currentEl == "w":
                wCounter += 1
            else:
                bCounter += 1
    print(wCounter, bCounter)

    #
    # i = len(colors)
    # wendyTurn = True
    # while i >= 0:
    #     if not len(wendy) % 2 == 0:
    #         wendy.pop()


colors = "wwwbb"

gameWinner(colors)
