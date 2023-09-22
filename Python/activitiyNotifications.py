def activityNotifications(expenditure, d):
    cacheForMedian = []
    median = 0
    notifications = 0
    for i, num in enumerate(expenditure):
        n = len(cacheForMedian)
        if n == d:
            cacheToManipulate = cacheForMedian.copy()
            cacheToManipulate.sort()
            if n % 2 == 0:
                median = (cacheToManipulate[n // 2 - 1] + cacheToManipulate[n // 2]) / 2
            else:
                median = cacheToManipulate[n // 2]
            # Below sets up for next iteration, removing index 0 and appending new value
            if num >= median * 2:
                notifications += 1
            cacheForMedian.pop(0)
            cacheForMedian.append(cacheForMedian[min(i + 1, len(cacheForMedian) - 1)])

        else:
            cacheForMedian.append(num)

    return notifications


# I think the above returns properly, but it's very inefficient and times out

expenditure = [2, 3, 4, 2, 3, 6, 8, 4]
d = 5

print(activityNotifications(expenditure, d))
