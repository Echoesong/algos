def maximumToys(prices, k):
    prices.sort()
    total = 0
    count = 0
    for num in prices:
        if total <= k:
            total += num
            count += 1
            if total > k:
                total -= num
                count -= 1
                return count


prices = [2, 1, 3, 4]
k = 7
print(maximumToys(prices, k))
