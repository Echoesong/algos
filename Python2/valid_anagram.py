# What is an anagram? A word with the same number of character occurances as another word.
# So, we can create an empty dictionary, then loop over s; if char is in dictionary, increment value by 1; otherwase, create new key-value with char : 0
# At the end, we can check if the dictionaries for each are the same.


def isAnagram(s, t):
    if not len(s) == len(t):
        return False
    dict = {}
    other_dict = {}
    for char in s:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    for char in t:
        if char not in other_dict:
            other_dict[char] = 1
        else:
            other_dict[char] += 1
    if dict.items() == other_dict.items():
        return True
    else:
        return False


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
