# Possible route to get around timeout issues: Only sort cacheForMedian once when it is the proper length, then after that add the elements in a sorted manner

import bisect


def activityNotifications(expenditure, d):
    cacheForMedian = []
    notifications = 0
    sorted = False
    for i, num in enumerate(expenditure):
        n = len(cacheForMedian)
        # if cacheForMedian is as long as the # of days, and it's not sorted, sort it, and update sorted to True. This is just a check to kickstart the sorting of cacheForMedian
        if n == d and sorted == False:
            cacheForMedian.sort()
            sorted = True
        # if cacheForMedian is as long as the # of days,
        if n == d:
            # if length of cacheForMedian is even, it equals the if statement; if odd, equals the else statement
            if n % 2 == 0:
                median = (cacheForMedian[n // 2 - 1] + cacheForMedian[n // 2]) / 2
            else:
                median = cacheForMedian[n // 2]
            # if number is greater than or equal to twice the median, it gets 'flagged' and notifications increase by 1
            if num >= median * 2:
                notifications += 1
            # indexToRemove is the oldest/stalest entry in cacheForMedian, calculated by current index minus # of days
            indexToRemove = i - d
            # Remove the first value in cacheForMedian equal to the expenditure[indexToRemove] value
            cacheForMedian.remove(expenditure[indexToRemove])
            # Insert the current num in proper median order0
            bisect.insort(cacheForMedian, num)

        # If cacheForMedian isn't long enough yet, append the current num
        else:
            cacheForMedian.append(num)

    return notifications


# I think the above returns properly, but it's very inefficient and times out

expenditure = [10, 20, 30, 40, 50]
d = 3

print(activityNotifications(expenditure, d))
