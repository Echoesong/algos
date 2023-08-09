# Okay, so we'll have to start with list1[0] compared to list2[0] and see which is lower. This will be our starting to add to the output;

# Then, depending on which list we are in, we will want to check if the numbers in the range of our first number and the next one in our list is in the other list; if so, append that/those numbers to the new list, and update our left opinter.

# Seems like a 2 pointer solution would work, with the left pointer being our 'earliest' value in one of the lists, the right pointer being the next element; if the other list has values between the range, we add them and make the new left pointer the


def mergeTwoLists(list1, list2):
    list1.extend(list2)
    list1.sort()
    return list1
    pass


list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(mergeTwoLists(list1, list2))
