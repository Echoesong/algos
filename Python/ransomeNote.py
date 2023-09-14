#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#


def checkMagazine(magazine, note):
    magazineDict = {}
    noteDict = {}
    output = "Yes"
    for word in magazine:
        if word in magazineDict.values():
            magazineDict[word] += 1
        else:
            magazineDict.update({word: 1})
    for word in note:
        if word in noteDict:
            noteDict[word] += 1
        else:
            noteDict.update({word: 1})
    print(magazineDict, noteDict)
    for word in noteDict:
        if word in magazineDict:
            if magazineDict[word] >= noteDict[word]:
                magazineDict[word] -= 1
                noteDict[word] -= 1
                continue
            else:
                output = "No"
        else:
            output = "No"
    print(output)


checkMagazine(
    ["two", "times", "three", "is", "not", "four"],
    ["two", "times", "two", "is", "four"],
)
