# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict

# The below implementation uses a hash map / dictionary where the key is a tuple of the # of occurances of letters for a word, and the value is all strings that result in that same count. 
def group_anagrams(strs):
    res = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for letter in word:
            count[ord(letter) - ord("a")] += 1
        res[tuple(count)].append(word)  
    return res.values()  


print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
