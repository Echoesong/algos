# Change for comment's sake
def isAnagram(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False


s = "jar"
t = "jam"

print(isAnagram(s, t))


def isAnagram2(string1, string2):
    myDict = {}
    for letter in string1:
        if letter in myDict.keys():
            myDict[letter] += 1
        else:
            myDict.update({letter: 1})
    for letter in string2:
        if letter in myDict.keys():
            myDict[letter] -= 1
        else:
            return False
    for number in myDict.values():
        if number == 0:
            continue
        else:
            return False
    return True


s = "racecar"
t = "carrace"
print(isAnagram2(s, t))
