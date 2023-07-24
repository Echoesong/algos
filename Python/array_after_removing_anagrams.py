words = ["abba","baba","bbaa","cd","cd"]
def remove_anagrams(words):
    for i in range(len(words)-1, 0, -1):
            if sorted(words[i]) == sorted(words[i-1]):
                del words[i]
    return words

