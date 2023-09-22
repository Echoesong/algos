# Possible route to get around timeout issues: Only sort cacheForMedian once when it is the proper length, then after that add the elements in a sorted manner

import bisect


def activityNotifications(expenditure, d):
    cacheForMedian = []
    notifications = 0
    sorted = False
    for i, num in enumerate(expenditure):
        n = len(cacheForMedian)
        if n == d and sorted == False:
            cacheForMedian.sort()
            sorted = True
        if n == d:
            indexToRemove = i - d
            if n % 2 == 0:
                median = (cacheForMedian[n // 2 - 1] + cacheForMedian[n // 2]) / 2
            else:
                median = cacheForMedian[n // 2]
            if num >= median * 2:
                notifications += 1
            # Below section 'resets' the cache to it's unsorted value--
            # Sets up cache for next iteration
            cacheForMedian.remove(expenditure[indexToRemove])
            bisect.insort(cacheForMedian, num)

        else:
            cacheForMedian.append(num)

    return notifications


# I think the above returns properly, but it's very inefficient and times out

expenditure = [10, 20, 30, 40, 50]
d = 3

print(activityNotifications(expenditure, d))
