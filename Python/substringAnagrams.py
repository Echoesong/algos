def sherlockAndAnagrams(s):
    import math

    dict = {}
    count = 0
    for i, char in enumerate(s):
        j = i + 1
        while j <= len(s):
            subString = s[i:j]
            sortedSubString = "".join(sorted(list(subString)))
            if not sortedSubString in dict.keys():
                dict[sortedSubString] = 1
            else:
                dict[sortedSubString] += 1
            j += 1
    for key, val in dict.items():
        print(dict.keys())
        print(dict.values())
        if val > 1:
            count += val * (val - 1) / 2
        print("Count: ", count)
    return math.floor(count)


s = "mom"
print(sherlockAndAnagrams(s))
