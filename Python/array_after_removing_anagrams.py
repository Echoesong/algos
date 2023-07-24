from ast import List


words = ["abba","baba","bbaa","cd","cd"]
def remove_anagrams(words):
    for i in range(len(words)-1, 0, -1):
            if sorted(words[i]) == sorted(words[i-1]):
                del words[i]
    return words

def remove_anagrams2(words):
        i = 0
        while i < len(words)-1:
            if sorted(words[i]) == sorted(words[i+1]):
                del words[i]
            else:
                i += 1
        return words
    
print(remove_anagrams(words))
print(remove_anagrams2(words))

# The above solutions achieve the same end, but 1 is more 'Pythonic,' whereas 2 is more easily understood 'at a glance.'
