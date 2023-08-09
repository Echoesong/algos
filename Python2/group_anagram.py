# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:


from collections import defaultdict


def groupAnagram(strs):
    myDict = defaultdict(dict)
    for word in strs:
        myDict[word] = 0
    for word in myDict:
        word.
    pass


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagram(strs)
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
