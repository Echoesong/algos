def sherlockAndAnagrams(s):
    dict = {}
    count = 0
    for char in s:
        if char in dict:
            dict[char] += 1
        else:
            dict.update({char: 1})

    while any(value > 0 for value in dict.values()):
        stringArr = []
        for char in dict:
            stringArr.extend(char * dict[char])
            comparisonDict = {}
            if stringArr == stringArr.reverse():
                count += 1
            if dict[char] > 0:
                dict[char] -= 1
        print(dict.values())
    return count


s = "mom"
print(sherlockAndAnagrams(s))
