def checkMagazine(magazine, note):
    noteDict = {}
    for word in note.split():
        noteDict.update({word: []})
    magazineWords = magazine.split()
    for word in noteDict:
        if word in magazineWords:
            print(magazineWords)
            noteDict[word].append(True)
            magazineWords.remove(word)
        else:
            noteDict[word].append(False)
    print(noteDict.values())
    if False in noteDict.values():
        print("No")
    else:
        print("Yes")


checkMagazine("two times three is not four", "two times two is four")
