def countSwaps(a):
    count = 0
    for i, num in enumerate(a):
        j = i + 1
        while j <= len(a):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
                count += 1
            else:
                continue
    print(count)


a = [3, 2, 1]
countSwaps(a)
