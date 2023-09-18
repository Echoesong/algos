def sherlockAndAnagrams(s):
    dict = {}
    count = 0
    for i, char in enumerate(s):
        j = i + 1
        while j <= len(s) - i:
            subString = s[i, j]
            subString.sort()
            if dict[subString] == 0:
                dict[subString] = 1
            else:
                dict[subString] += 1
            j += 1
    for key, val in dict.items():
        if val > 1:
            count += val * val(-1) / 2
    return count


s = "mom"
print(sherlockAndAnagrams(s))
